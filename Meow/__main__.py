import glob
import os
import sys
from sys import argv
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from Meow import LOGS, bot ,Config
from Meow.Config import Var
from Meow.utils import load_module,start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from Meow import CMD_HNDLR

MEOW = Var.PRIVATE_GROUP_ID
LOAD_MYBOT = Var.LOAD_MYBOT

# let's get the bot ready
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)

async def startup_log_all_done():
    try:
        await bot.send_message(Meow, f"**Meow π±πΎπ πΈπ π³π΄πΏπ»πΎππ΄π³.\nππ΄π½π³** `{CMD_HNDLR}alive` **ππΎ ππ΄π΄ π±πΎπ πΈπ ππΎππΊπΈπ½πΆ πΎπ π½πΎπ.\n\nAdd** @{BOTNAME} **π°π³π³ ππΎ ππ·πΈπ πΈπ½ ππΎππ πΆππΎππΏ π°π½π³ πΌπ°πΊπ΄ π·πΈπΌ π°π³πΌπΈπ½ π΅πΎπ π΄π½π°π±π»πΈπ½πΆ π°π»π» ππ·π΄ π΅π΄π°ππππ΄π πΎπ΅ π»ucifer π±πΎπ**")
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")
    else:
        bot.start()

path = 'Meow/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "Meow/plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("TGBot set up completely!")

print("TGBot set up - Level - Basic")
print(
    """
                ----------------------------------------------------------------------
                    Meow X 2.0 Κα΄s Κα΄α΄Ι΄ α΄α΄α΄Κα΄Κα΄α΄, α΄α΄ α΄ ΙͺsΙͺα΄ @Meow_support_group !!
                    Meow α΄ α΄Κ: V2.2
                    Β©Tα΄α΄α΄ Κucifer
                ----------------------------------------------------------------------
"""
)

# that's life...
# Join MeowBot Channel after deploying π€π
    try:
        await bot(JoinChannelRequest("@Murat_30_God"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@Meow_userbot"))
#    except BaseException:
#        pass


bot.loop.create_task(Meow_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# Meowbot
