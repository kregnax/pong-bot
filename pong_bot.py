import discord
import asyncio
from bs4 import BeautifulSoup
import urllib.request
import re

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

@client.event
async def on_message(message):
    if(message.content.startswith('!ping')):
        await client.send_message(message.channel, 'Pong!')
    if(message.content.startswith('!gameplan')):
        await client.send_message(message.channel, 'stop suk')
    if(message.content.startswith('!whothrew')):
        await client.send_message(message.channel, 'Diablo')
    if(message.content.startswith('!patchnotes')):
        url = 'http://us.battle.net/heroes/en/blog/'
        patch_note_base_url = 'http://us.battle.net'
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        link = soup.find('a', href = re.compile('heroes-of-the-storm-patch-notes'))['href']
        patch_notes_link = patch_note_base_url + link
        await client.send_message(message.channel, patch_notes_link)
    if(message.content.startswith('!commands')):
        await client.send_message(message.channel, 'Available commands:\n!ping\n!gameplan\n!whothrew\n!patchnotes')
client.run('MzYzMTEzNDY0NTg0OTk0ODE4.DK8fZw.u69xqQC76fYfozoKkGfZueaUgtc')