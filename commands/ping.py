def ping_msg():
    return "Pong ! :3"

def ping_embed(used_commands, total_messages_read):
    import discord
    ping_embed = discord.Embed (
        title       = "Pong ! :3",
        description = "Détermine le ping du bot !",
        color       = 0x00ff00
        )
    ping_embed.add_field (
        name   = "Latence",
        value  = str(round(client.latency * 1000)),
        inline = False
        )
    ping_embed.add_field (
        name   = "Nombre de commandes effectuées :",
        value  = str(used_commands)
    )
    ping_embed.add_field (
        name   = "Nombre de messages lus :",
        value  = str(total_messages_read)
    )
    return ping_embed