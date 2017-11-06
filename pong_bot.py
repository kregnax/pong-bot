import discord
import asyncio
from bs4 import BeautifulSoup
import urllib.request
import random
import re
import sys
import os
import json
import json_loader
import requests
import time
from voice_manager import VoiceManager

client = discord.Client()
configs = json_loader.get_json("config.json")
voice_files_location = configs["voice"]["directory_name"]
voice_manager = VoiceManager(client, voice_files_location)
voice_commands = voice_manager.get_voice_commands()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')
    #print(fetch.test_print_all())
    if sys.maxsize > 2**32:
        discord.opus.load_opus('libopus-0.x64.dll')
    else:
        discord.opus.load_opus('libopus-0.x86.dll')

@client.event
async def on_message(message):
    if(message.content.startswith("!voice")):
        await voice_manager.add_to_queue(message)
    if(message.content == "?voice"):
        commands = voice_manager.get_voice_command_help()
        await client.send_message(message.channel, commands)
    if(message.content.startswith('!garbagewater')):
        await voice_manager.play_audio(message, '.voice_lines/special/garbagewater.mp3', .15)
    if(message.content.startswith('!momma')):
        url = 'https://biffthecamel.herokuapp.com/yomomma'
        r = requests.get(url)
        joke = r.text
        input_text = ' '.join(message.content.split()[1:])
        rq = requests.get('https://biffthecamel.herokuapp.com/tts?t={}'.format(joke), stream=True)
        local_file_path = '.temp/{}.mp3'.format(int(time.time()))
        with open(local_file_path, 'wb') as f:
            for chunk in rq.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
            f.close()
        await voice_manager.add_to_queue(message, local_file_path)
    if(message.content.startswith('!tts')):
        input_text = ' '.join(message.content.split()[1:])
        r = requests.get('https://biffthecamel.herokuapp.com/tts?t={}'.format(input_text), stream=True)
        local_file_path = '.temp/{}.mp3'.format(int(time.time()))
        with open(local_file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
            f.close()
        await voice_manager.add_to_queue(message, local_file_path)
client.loop.create_task(voice_manager.consume_queue())
client.run('MzYzMTEzNDY0NTg0OTk0ODE4.DLMxNA.K-z0tleRpvrNykggsmUP5VZ56SI')