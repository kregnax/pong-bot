import discord
import asyncio
import json
import json_loader
import sys
import random
import os
import numbers


class VoiceManager(object):
    """This class manages the creation of voice players for the bot"""

    def __init__(self, client, voice_files_location):
        self.client = client
        self.voice_files_location = voice_files_location
        self.voice_commands = json_loader.get_json("voice_commands_alias.json")
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
                        if(direct_path_to_file is not None and direct_path_to_file.startswith('.temp')):
                            os.remove(direct_path_to_file)
                        await voice.disconnect()
                        break
                except:
                    break

    def get_path_to_selected_file(self, message):
        commands = str(message.content).split()
        command_length = len(commands)
        if(commands[0] == "!voice" and command_length >= 2):
            owner = str(commands[1])
            if(owner in self.voice_commands):
                selected_line = ''
                if(command_length >= 3):
                    alias = commands[2]
                    try:
                        selected_line = self.voice_commands[owner]["filename"][alias]
                    except:
                        random_line = random.choice(list(self.voice_commands[owner]["filename"].keys()))
                        selected_line = self.voice_commands[owner]["filename"][random_line]
                else:
                    random_line = random.choice(list(self.voice_commands[owner]["filename"].keys()))
                    selected_line = self.voice_commands[owner]["filename"][random_line]
                return '{}/{}/{}'.format(self.voice_files_location, owner, selected_line)

    def get_voice_commands(self):
        return self.voice_commands

    def get_voice_command_help(self):
        commands = 'Available voice lines:\n';
        for owner, v in self.voice_commands.items():
            commands += '\t__{}__\n'.format(owner)
            for ind, filenames in v.items():
                for alias, filename in filenames.items():
                    commands += '\t\t{} : {}\n'.format(alias, filename)
        commands += ("Typing !voice followed by a category (e.g. !voice genji) will "+
                     "play a random file from that category. To play a specific file, type "+
        "!voice category followed by the alias of the file. !voice genji become will play "+
        "'The Dragon Becomes Me!'")
        return commands
