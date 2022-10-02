TOKEN = 'ODMzMzM0ODYzMzg5OTE3MjI0.G7oD0y.RxHDYYunl9cu6mNExToVKZuN3XrFwVbRzi8WsA'

# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'{message.author}: {message.content}')
        # don't respond to ourselves
        if message.author == self.user:
            return

        if 'ping' in message.content:
            await message.channel.send('Pong ! :3')
            
        if 'hello' in message.content:
            await message.channel.send('Hello ! ✌')
            
        if 'bye' in message.content:
            await message.channel.send('Bye ! 👋')

        if 'help' in message.content:
            await message.channel.send("Voici un message d'aide !\nToutes les commandes disponibles :\n- ping\n- hello\n- bye\n- help\n||(Oui je sais la présentation est pas belle pour l'instant ;-;)||")
            
        if 'test' in message.content:
            await message.channel.send('Test réussi !')
        
        if 'website' in message.content:
            website = discord.Embed (
                title = "Le site web Exaload",
                url = "https://exaload.glitch.me/",
                description = "Voici une petite présentation du projet Exaload",
                color = 0x333333
                )
            website.set_footer (
                text = "Made with ❤ by Un Thomas Sauvage !!#1309",
                icon_url = "https://cdn.discordapp.com/avatars/755738381455065120/94e36a128d280a8a79fe847a0a10a379.webp?size=1024"
                )
            website.add_field (
                    name = "Notre équipe",
                    value = "Nous sommes actuellement composé de 6 personnes :\n- Un Thomas Sauvage !!#1309\n- D4RTH36dious#2007\n- aymanouse#8586\n- Adriwin#7410\n- Kiverix#8301\n- Truzz™#3826",
                    
                )
            
            await message.channel.send(embed = website)
            

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('ODMzMzM0ODYzMzg5OTE3MjI0.G7oD0y.RxHDYYunl9cu6mNExToVKZuN3XrFwVbRzi8WsA')