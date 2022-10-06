from random import *
def help_msg():
    import discord
    msg_help_alt_list = [
        "Vous avez demandé de l'aide ? 😎",
        "Un message d'aide sauvage !!",
        "OH MON DIEU UN MESSAGE D'AIDE !!",
        "Vous avez besoin d'aide ? ;-;"
    ]
    
    help_embed = discord.Embed(
        title = msg_help_alt_list[randint(0, len(msg_help_alt_list) - 1)],
        color = 0xffffff,
        description = "Je vais essayer de t'aider !"
    )
    
    help_embed.add_field (
        name = "help",
        value = "e"
    )
    
    return help_embed