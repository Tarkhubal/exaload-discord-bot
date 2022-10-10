from random import *
from lang.lang_translate import *

def help_msg():
    import discord
    msg_help_alt_list = lang_obj_fr_fr['help_alt']

    help_embed = discord.Embed(
        title=msg_help_alt_list[randint(0, len(msg_help_alt_list) - 1)],
        color=0xffffff,
        description="Je vais essayer de t'aider !"
    )
    help_embed.add_field(
        name="Pour les commandes suivantes, le bot y répondra même sans mettre de préfix !",
        value="_Essaie d'écrire une belle phrase avec ces mots pour voir !_",
        inline=False
    )

    help_embed.add_field(
        name="help",
        value="Génère cette aide !",
        inline=True
    )
    help_embed.add_field(
        name="website",
        value="Génère un joli message avec pleins d'informations sur le site web [Exaload](https://exaload.glitch.me) !",
        inline=True
    )
    help_embed.add_field(
        name="ping",
        value="Un petit ping pour voir si le bot est en ligne :3",
        inline=True
    )
    help_embed.add_field(
        name="hello",
        value="Le bot te dis bonjour ! 👋",
        inline=True
    )
    help_embed.add_field(
        name="bye",
        value="Et là il te dit au revoir >:3",
        inline=True
    )
    help_embed.add_field(
        name="tg",
        value="C'est pas cool de dire ça au bot :(",
        inline=True
    )

    return help_embed
