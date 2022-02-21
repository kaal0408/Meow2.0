import glob
import os
import sys
from sys import argv
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from userbot import LOGS, bot
from .Config import Var
from userbot.utils import load_module,start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from userbot import CMD_HNDLR

MEOW = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT

# let's get the bot ready
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)

async def startup_log_all_done():
    try:
        await bot.send_message(Meow, f"**Meow 2.0 𝙱𝙾𝚃 𝙸𝚂 𝙳𝙴𝙿𝙻𝙾𝚈𝙴𝙳.\n𝚂𝙴𝙽𝙳** `{CMD_HNDLR}alive` **𝚃𝙾 𝚂𝙴𝙴 𝙱𝙾𝚃 𝙸𝚂 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙾𝚁 𝙽𝙾𝚃**")
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")

# Meowbot starter...
# chal jana bdsk🤧 
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "userbot/plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("MeowBot set up completely!")

print("MeowBot set up - Level - Basic")
print(
    """
                ----------------------------------------------------------------------
                    Meow  2.0 ʜᴀs ʙᴇᴇɴ ᴅᴇᴘʟᴏʏᴇᴅ, ᴅᴏ ᴠɪsɪᴛ @Murat_30_God !!
                    Meow ᴠᴇʀ: V2.2
                    ©Team Meow
                ----------------------------------------------------------------------
"""
)

# that's life...
async def Meow_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                caption=f"#START \n\nDeployed MeowBot Successfully\n\n**Meow - {Meowver}**\n\nType {hl}ping or {hl}alive to check! \n\nJoin [Meow Channel](t.me/MeowXupdates) for Updates & [Meow Chat](t.me/Meow_support_group) for any query regarding Meowẞø†",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join MeowBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Murat_30_God"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@MeowUserbot"))
#    except BaseException:
#        pass


bot.loop.create_task(Meow_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# Meowbot
