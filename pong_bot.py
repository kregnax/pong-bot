import discord
import asyncio
from bs4 import BeautifulSoup
import urllib.request
import re
import sys
from os import listdir
import json
import tempfile
import json_loader

client = discord.Client()

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
    if(message.content.startswith("!addtxtcmd")):
        if(str(message.author) == "kregnax#2710"):
            cmd_in = str(message.content).split()
            if(cmd_in[0] == "!addtxtcmd"):
                text_commands[cmd_in[1]] = ''.join(w+' ' for w in cmd_in[2:]).strip()
                temp_json = json.dumps(text_commands)
                temp_json = json.loads(temp_json)
                with open('text_commands.json','w') as f:
                    json.dump(temp_json, f,indent=4)
            else:
                await client.send_message(message.channel, "Unrecognized command: "+cmd_in[0])
        else:
            await client.send_message(message.channel, "You don't have access, pleb.")
    if(str(message.content) == "?text"):
        commands = 'Available text commands:\n';
        for k, v in text_commands.items():
            commands += "!"+k+"\n"
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
    if(message.content.startswith('!genjivoice')):
        author = message.author
        v_channel = author.voice.voice_channel
        if(v_channel is not None):
            voice = await client.join_voice_channel(v_channel)
            player = voice.create_ffmpeg_player('.voice_lines/genji/mada_mada.mp3')
            player.start()
            while True:
                try:
                    if player.is_done():
                        await voice.disconnect()
                        break
                except:
                    break;
    if(message.content.startswith('!hagay')):
        author = message.author
        v_channel = author.voice.voice_channel
        if(v_channel is not None):
            voice = await client.join_voice_channel(v_channel)
            player = voice.create_ffmpeg_player('.voice_lines/misc/hagay.mp3')
            player.start()
            while True:
                try:
                    if player.is_done():
                        await voice.disconnect()
                        break
                except:
                    break;
    if(message.content.startswith('!commands')):
        await client.send_message(message.channel, 'Available commands:\n!ping\n!gameplan\n!whothrew\n!patchnotes')


configs = json_loader.get_json("config.json")
text_commands = json_loader.get_json("text_commands.json")
voice_commands = json_loader.get_json("voice_commands.json")
client.run('MzYzMTEzNDY0NTg0OTk0ODE4.DK8fZw.u69xqQC76fYfozoKkGfZueaUgtc')