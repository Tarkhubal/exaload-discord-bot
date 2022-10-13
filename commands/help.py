from random import *
from lang.lang_translate import *

def help_msg():
    import discord
    msg_help_alt_list = lang_obj_fr_fr['help_alt']

    help_embed = discord.Embed(
        title=msg_help_alt_list[randint(0, len(msg_help_alt_list) - 1)],
        color=0xffffff,
        description= lang_obj_fr_fr['help_desc']
    )
    
    
    help_embed.add_field(
        name= lang_obj_fr_fr['help_title'],
        value= lang_obj_fr_fr['help_desc'],
        inline=False
    )

    help_embed.add_field(
        name="help",
        value= lang_obj_fr_fr['help_command__help'],
        inline=True
    )
    help_embed.add_field(
        name="website",
        value= lang_obj_fr_fr['help_command__website'],
        inline=True
    )
    help_embed.add_field(
        name="stats",
        value= lang_obj_fr_fr['help_command__stats'],
        inline=True
    )
    help_embed.add_field(
        name="hello",
        value= lang_obj_fr_fr['help_command__hello'],
        inline=True
    )
    help_embed.add_field(
        name="bye",
        value= lang_obj_fr_fr['help_command__bye'],
        inline=True
    )
    help_embed.add_field(
        name="tg",
        value= lang_obj_fr_fr['help_command__tg'],
        inline=True
    )

    return help_embed
