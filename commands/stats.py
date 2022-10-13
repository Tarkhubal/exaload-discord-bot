from lang.lang_translate import *


def stats_msg():
    return "Pong ! :3"


def stats_embed(used_commands, total_messages_read):
    import discord
    stats_embed = discord.Embed(
        title= lang_obj_fr_fr['stats_title'],
        description= lang_obj_fr_fr['stats_desc'],
        color=0x00ff00
    )
    stats_embed.add_field(
        name="Latence",
        value=str(round(client.latency * 1000)),
        inline=False
    )
    stats_embed.add_field(
        name="Nombre de commandes effectuées :",
        value=str(used_commands)
    )
    stats_embed.add_field(
        name="Nombre de messages lus :",
        value=str(total_messages_read)
    )
    return stats_embed
