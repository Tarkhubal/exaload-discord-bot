TOKEN = 'your token here'

# This example requires the 'message_content' intent.

import discord
from random import *

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'{message.author}: {message.content}')
        
        # file = open('log.txt', 'a')
        # file.write('\n' + f'{message.channel} / {message.author}: {message.content}' + '\n')
        # file.close()
        
        # don't respond to ourselves
        if message.author == self.user:
            return

        if 'ping' in message.content:
            await message.channel.send('Pong ! :3')
            
        if 'hello' in message.content:
            msg_hello_alt_list = ['Hello ! ✌', 'Hi !!', 'Hey !', 'Hi ! :3']
            await message.channel.send(msg_hello_alt_list[randint(0, len(msg_hello_alt_list) - 1)])
            
        if 'bye' in message.content:
            msg_bye_alt_list = ['Bye ! 👋', 'Bye !', 'Bye ! :3' 'Goodbye :3']
            await message.channel.send(msg_bye_alt_list[randint(0, len(msg_bye_alt_list) - 1)])

        if 'help' in message.content:
            # await message.channel.send("Voici un message d'aide !\nToutes les commandes disponibles :\n- ping\n- hello\n- bye\n- help\n||(Oui je sais la présentation est pas belle pour l'instant ;-;)||")
            msg_help_alt_list = ["Vous avez demandé de l'aide ? 😎", "Un message d'aide sauvage !!", "OH MON DIEU UN MESSAGE D'AIDE !!", "Vous avez besoin d'aide ? ;-;"]
            help = discord.Embed (
                    title = msg_help_alt_list[randint(0, len(msg_help_alt_list) - 1)],
                    color = 0xffffff
                )
            await message.channel.send(embed = help)
            
        if 'test' in message.content:
            await message.channel.send('Test réussi !')
            
        if 'tg' in message.content:
            await message.channel.send("C'est pas très gentil tout ça Baku :(")
        
        if 'website' in message.content:
            website = discord.Embed (
                title = "Le site web Exaload",
                url = "https://exaload.glitch.me/",
                description = "Voici une petite présentation du projet Exaload",
                color = 0xffffff
                )
            website.set_footer (
                text = "Made with ❤ by Un Thomas Sauvage !!#1309",
                icon_url = "https://cdn.discordapp.com/avatars/755738381455065120/94e36a128d280a8a79fe847a0a10a379.webp?size=1024"
                )
            website.add_field (
                    name = "Notre objectif",
                    value = "Notre objectif est de créer un site internet qui rassemblerait tous les jeux, les films, les musiques ou encore les séries. SAUF que tout cela serait accessible gratuitement (voir sur le site pour plus d'informations)",
                    inline = False
                )
            website.add_field (
                    name = "Nos réseaux sociaux",
                    value = "Chez Exaload, on aime vous écouter, donc on essaie d'être disponibles au max sur les réseaux sociaux pour que vous puissiez nous donner toutes vos impressions sur notre projet !\n\nVoici la liste de nos comptes :\n- [Discord](https://discord.gg/2FjfpXavSF)\n- [Twitter](https://www.twitter.com/exa_load)\n- [Instagram](https://www.instagram.com/exaload)\n\n(et d'autres encore mais flemme de remplir la description avec ça pour le moment xD)",
                )
            website.add_field (
                    name = "Notre équipe",
                    value = "Nous équipe est actuellement composée de 6 personnes :\n- Un Thomas Sauvage !!#1309\n- D4RTH36dious#2007\n- aymanouse#8586\n- Adriwin#7410\n- Kiverix#8301\n- Truzz™#3826"
                )
            await message.channel.send(embed = website)
            

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)