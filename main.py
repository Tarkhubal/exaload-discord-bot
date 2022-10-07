TOKEN = 'your token here'

# This example requires the 'message_content' intent.

import discord
from random import *
from all_commands import *
from discord.utils import *
import os
from json import *

used_commands  = 0
total_messages_read = 0

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user} !')

    async def on_message(self, message):
        print(f'{message.author}: {message.content}')
        total_messages_read += 1
        
        # don't respond to ourselves
        if message.author == self.user:
            return

        if 'ping' in message.content:
            used_commands += 1
            await message.channel.send(embed = ping_embed(used_commands, total_messages_read))
            
        if 'hello' in message.content:
            await message.channel.send(hello_msg())
            used_commands += 1
            
        if 'bye' in message.content:
            await message.channel.send(bye_msg())
            used_commands += 1

        if 'help' in message.content:
            await message.channel.send(embed = help_msg())
            used_commands += 1
            
        if 'tg' in message.content:
            await message.channel.send(tg_msg())
            used_commands += 1
        
        if 'website' in message.content:
            await message.channel.send(embed = website_embed())
            used_commands += 1
        
        if 'random' in message.content:
            # to create
            await message.channel.send("Une commande à venir !!")
            


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)