from commands.lang.lang_translate import *

def website_embed():
    import discord

    website_embed = discord.Embed(
        title =         lang_obj_fr_fr['website_title'],
        url =           lang_obj_fr_fr['website_url'],
        description =   lang_obj_fr_fr['website_desc'],
        color=          0xffffff
    )
    website_embed.set_footer(
        text =          lang_obj_fr_fr['website_footer_title'],
        icon_url =      lang_obj_fr_fr['website_footer_icon']
    )
    website_embed.add_field(
        name =          lang_obj_fr_fr['objective'],
        value =         lang_obj_fr_fr['objective_desc'],
        inline =        False
    )
    website_embed.add_field(
        name =          lang_obj_fr_fr['social_nets'],
        value =         lang_obj_fr_fr['social_nets_desc'],
    )
    website_embed.add_field(
        name =          lang_obj_fr_fr['equip'],
        value =         lang_obj_fr_fr['equip_desc']
    )

    return website_embed
