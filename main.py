TOKEN = 'your token here'

# This example requires the 'message_content' intent.

import discord
from random import *
from all_commands import *

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user} !')

    async def on_message(self, message):
        print(f'{message.author}: {message.content}')
        
        # don't respond to ourselves
        if message.author == self.user:
            return

        if 'ping' in message.content:
            await message.channel.send(ping_msg())
            
        if 'hello' in message.content:
            await message.channel.send(hello_msg())
            
        if 'bye' in message.content:
            await message.channel.send(bye_msg())

        if 'help' in message.content:
            await message.channel.send(embed = help_msg())
            
        if 'tg' in message.content:
            await message.channel.send(tg_msg())
        
        if 'website' in message.content:
            await message.channel.send(embed = website_embed())
            

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)