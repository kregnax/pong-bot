import discord
import asyncio
from bs4 import BeautifulSoup
import urllib.request
import random
import re
import sys
import os
import json
import tempfile
import json_loader
import requests
from voice_manager import VoiceManager

client = discord.Client()
configs = json_loader.get_json("config.json")
text_commands = json_loader.get_json("text_commands.json")
voice_commands = json_loader.get_json("voice_commands.json")
voice_files_location = configs["voice"]["directory_name"]
voice_manager = VoiceManager(client, voice_files_location)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')
    if sys.maxsize > 2**32:
        discord.opus.load_opus('libopus-0.x64.dll')
    else:
        discord.opus.load_opus('libopus-0.x86.dll')

@client.event
async def on_message(message):
    #TODO: use message.attachments to save images with text command
    if(message.content.startswith("!voice")):
        await voice_manager.play_audio(message)
    if(message.content.startswith("!addtxtcmd")):
        if(str(message.author) == "kregnax#2710"):
            cmd_in = message.content.split()
            if(cmd_in[0] == "!addtxtcmd"):
                text_commands[cmd_in[1]] = ''.join(w+' ' for w in cmd_in[2:]).strip()
                temp_json = json.dumps(text_commands)
                temp_json = json.loads(temp_json)
                with open('text_commands.json','w') as f:
                    json.dump(temp_json, f,indent=4)
            else:
                await client.send_message(message.channel, "Unrecognized command: {}".format(cmd_in[0]))
        else:
            await client.send_message(message.channel, "You don't have access, pleb.")
    if(message.content == "?text"):
        commands = 'Available text commands:\n';
        for k, v in text_commands.items():
            commands += "!{}\n".format(k)
        await client.send_message(message.channel, commands)
    if(message.content == "?voice"):
        commands = 'Available voice lines:\n';
        for owner, v in voice_commands.items():
            commands += "\t{}\n".format(owner)
            for ind, filename in v.items():
                for index, file in enumerate(filename):
                    commands += "\t\t{}: {}\n".format(str(index+1), file)
        commands += ("Typing !voice followed by a category (e.g. !voice genji) will "+
        "play a random file from that category. To play a specific file, type "+
        "!voice category followed by the index of the file. !voice genji 5 will play "+
        "'The Dragon Becomes Me!'")
        await client.send_message(message.channel, commands)
    if(message.content.startswith('!')):
        command = str(message.content).split()[0][1:]
        if(command in text_commands):
            await client.send_message(message.channel, text_commands[command])
    if(message.content.startswith('!patchnotes')):
        url = 'http://us.battle.net/heroes/en/blog/'
        patch_note_base_url = 'http://us.battle.net'
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        link = soup.find('a', href = re.compile('heroes-of-the-storm-patch-notes'))['href']
        patch_notes_link = patch_note_base_url + link
        await client.send_message(message.channel, patch_notes_link)
    if(message.content.startswith('!garbagewater')):
        await voice_manager.play_audio(message, '.voice_lines/special/garbagewater.mp3', .15)
    if(message.content.startswith('!momma')):
        url = 'https://biffthecamel.herokuapp.com/yomomma'
        r = requests.get(url)
        joke = r.text
        input_text = ' '.join(message.content.split()[1:])
        rq = requests.get('https://biffthecamel.herokuapp.com/tts?t={}'.format(joke), stream=True)
        local_file_path = '.temp/tempaudio.mp3'
        with open(local_file_path, 'wb') as f:
            for chunk in rq.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        await voice_manager.play_audio(message, local_file_path)
        os.remove(local_file_path)
    if(message.content.startswith('!tts')):
        input_text = ' '.join(message.content.split()[1:])
        r = requests.get('https://biffthecamel.herokuapp.com/tts?t={}'.format(input_text), stream=True)
        local_file_path = '.temp/tempaudio.mp3'
        with open(local_file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        await voice_manager.play_audio(message, local_file_path)
        os.remove(local_file_path)
    if(message.content.startswith('!commands')):
        await client.send_message(message.channel, 'Available commands:\n!ping\n!gameplan\n!whothrew\n!patchnotes')

client.run('MzYzMTEzNDY0NTg0OTk0ODE4.DLMxNA.K-z0tleRpvrNykggsmUP5VZ56SI')