def website_embed():
    import discord
    website_embed = discord.Embed(
        title="Le site web Exaload",
        url="https://exaload.glitch.me/",
        description="Voici une petite présentation du projet Exaload",
        color=0xffffff
    )
    website_embed.set_footer(
        text="Made with ❤ by Un Thomas Sauvage !!#1309",
        icon_url="https://cdn.discordapp.com/avatars/755738381455065120/94e36a128d280a8a79fe847a0a10a379.webp?size=1024"
    )
    website_embed.add_field(
        name="Notre objectif",
        value="Notre objectif est de créer un site internet qui rassemblerait tous les jeux, les films, les musiques ou encore les séries. SAUF que tout cela serait accessible gratuitement (voir sur le site pour plus d'informations)",
        inline=False
    )
    website_embed.add_field(
        name="Nos réseaux sociaux",
        value="Chez Exaload, on aime vous écouter, donc on essaie d'être disponibles au max sur les réseaux sociaux pour que vous puissiez nous donner toutes vos impressions sur notre projet !\n\nVoici la liste de nos comptes :\n- [Discord](https://discord.gg/2FjfpXavSF)\n- [Twitter](https://www.twitter.com/exa_load)\n- [Instagram](https://www.instagram.com/exaload)\n\n(et d'autres encore mais flemme de remplir la description avec ça pour le moment xD)",
    )
    website_embed.add_field(
        name="Notre équipe",
        value="Nous équipe est actuellement composée de 6 personnes :\n- Un Thomas Sauvage !!#1309\n- D4RTH36dious#2007\n- aymanouse#8586\n- Adriwin#7410\n- Kiverix#8301\n- Truzz™#3826"
    )

    return website_embed
