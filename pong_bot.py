import discord
import asyncio
from bs4 import BeautifulSoup
import urllib.request
import re
import sys
from os import listdir

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
    if(message.content.startswith('!ping')):
        await client.send_message(message.channel, 'Pong!')
    if(message.content.startswith('!gameplan')):
        await client.send_message(message.channel, 'stop suk')
    if(message.content.startswith('!whothrew')):
        author = str(message.author).split('#')[0]
        await client.send_message(message.channel, 'Either ' +author+ ' or Diablo. But probably '+author+'.')
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

client.run('MzYzMTEzNDY0NTg0OTk0ODE4.DK8fZw.u69xqQC76fYfozoKkGfZueaUgtc')