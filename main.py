from commands.lang.lang_translate import *
import os
from discord.utils import *
from all_commands import *
from random import *
import discord
from discord.ext import commands
from database.dataadd import *
from json import *


TOKEN = 'your token here'

# This example requires the 'message_content' intent.


used_commands = 0
total_messages_read = 0


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'' + lang_obj_fr_fr['logged'] +
              f' {self.user} (ID: {self.user.id})')
        await client.change_presence(activity=discord.Game(name="essayer de t'aider !"))

    async def on_message(self, message):
        
        #database = open("database/users.json", "a")
        # f not(message.author.id in database['']):
        #add = {message.author.id}
        #database.update(add)
        
        
        print(f'{message.author}: {message.content}')

        # don't respond to ourselves
        if message.author == self.user:
            return

        global total_messages_read
        global used_commands
        total_messages_read += 1

        if 'ping' in message.content:
            used_commands += 1
            await message.channel.send(embed=stats_embed(used_commands, total_messages_read))

        if 'hello' in message.content:
            await message.channel.send(hello_msg())
            used_commands += 1

        if 'bye' in message.content:
            await message.channel.send(bye_msg())
            used_commands += 1

        if 'help' in message.content:
            await message.channel.send(embed=help_msg())
            used_commands += 1

        if 'tg' in message.content:
            await message.channel.send(tg_msg())
            used_commands += 1

        if 'website' in message.content:
            await message.channel.send(embed=website_embed())
            used_commands += 1

        if 'random' in message.content:
            # to create
            await message.channel.send(lang_obj_fr_fr['future_commands'])


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
