import discord
import asyncio
import json
import json_loader
import sys
import random
import os


class VoiceManager(object):
    """This class manages the creation of voice players for the bot"""

    def __init__(self, client, voice_files_location):
        self.client = client
        self.voice_files_location = voice_files_location
        self.voice_commands = json_loader.get_json("voice_commands.json")
        self.voice_queue = asyncio.Queue()
        self.last_voice_command = ""

    async def add_to_queue(self, message, direct_path_to_file = None, volume = None):
            await self.voice_queue.put((message, direct_path_to_file, volume))

    async def consume_queue(self):
        await self.client.wait_until_ready()
        print("Initiating queue loop...")
        while not self.client.is_closed:
            next_comm = await self.voice_queue.get()
            await self.play_audio(next_comm[0], next_comm[1], next_comm[2])


    async def play_audio(self, message, direct_path_to_file = None, volume = None):
        author = message.author
        v_channel = author.voice.voice_channel
        if(v_channel is not None):
            voice = await self.client.join_voice_channel(v_channel)
            if(direct_path_to_file is None):
                player = voice.create_ffmpeg_player(self.get_path_to_selected_file(message))
            else:
                player = voice.create_ffmpeg_player(direct_path_to_file)
            if(volume is not None):
                player.volume = volume
            player.start()
            while True:
                try:
                    if player.is_done():
                        if(direct_path_to_file.startswith('.temp')):
                            os.remove(direct_path_to_file)
                        await voice.disconnect()
                        break
                except:
                    break;

    def get_path_to_selected_file(self, message):
        commands = str(message.content).split()
        command_length = len(commands)
        if(commands[0] == "!voice" and command_length >= 2):
            owner = str(commands[1])
            if(owner in self.voice_commands):
                available_lines = self.voice_commands[owner]["filename"]
                try:
                    index = int(commands[2])-1
                except:
                    index = 9999
                selected_line = ''
                if(command_length >= 3 and abs(index) <= len(available_lines)-1):
                    selected_line = str(available_lines[index])
                else:
                    selected_line = str(random.choice(available_lines))
                return '{}/{}/{}'.format(self.voice_files_location, owner, selected_line)

    def getLastVoiceCommand(self):
        return self.last_voice_command
    def setLastVoiceCommand(self, last_voice_command):
        self.last_voice_command = last_voice_command
