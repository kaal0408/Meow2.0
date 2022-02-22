import os
import re
import urllib
from math import ceil
from re import findall
from urllib.parse import quote

import requests
from search_engine_parser import GoogleSearch
from telethon import Button, custom, events, functions

from Meow import ALIVE_NAME, CMD_HELP, CMD_LIST
from Meow import inlinestats

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/3dd42b44d10528fa1f925.jpg"
else:
    WARN_PIC = PMPERMIT_PIC
LOG_CHAT = Config.PRIVATE_GROUP_ID
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Meow-X"

if lang == "si":

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Fire-X"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_HELP, "helpme")
            result = builder.article(
                "© Userbot Help",
                text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
            await event.answer([result])
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**Showing Stats For {DEFAULTUSER}'s Meow-XBot** \nNote --> Only Owner Can Check This \n(C) [Fire-X](https://github.com/TeamEviral/Fire-X)",
                buttons=[
                    [custom.Button.inline("Show Stats ?", data="terminator")],
                    [Button.url("Developed By", "https://github.com/kaal0408")],
                    [Button.url("Support Chat❤️", "t.me/MeowUserbot")],
                ],
            )
            await event.answer([result])
        elif event.query.user_id == bot.uid and query.startswith("**Hello"):
            result = builder.photo(
                file=WARN_PIC,
                text=query,
                buttons=[
                    [custom.Button.inline("Spamming", data="dontspamnigga")],
                    [
                        custom.Button.inline(
                            "Casual Talk",
                            data="whattalk",
                        )
                    ],
                    [custom.Button.inline("Requesting", data="askme")],
                ],
            )
            await event.answer([result])

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_popp_up_alert = "ඔය මොකද කරන්නෙ, මේක ඔයාගෙ නෙමේ!"
            await event.answer(reply_popp_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_HELP, "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "මොන පිස්සෙක්ද තෝ? උඹටම කියල බොටෙක් හදාගනිම්.!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if not event.query.user_id == bot.uid:
            sedok = "මොන පිස්සෙක්ද තෝ? උඹටම කියල බොටෙක් හදාගනිම්."
            await event.answer(sedok, cache_time=0, alert=True)
            return
        plugin_name = event.data_match.group(1).decode("UTF-8")
        if plugin_name in CMD_HELP:
            help_string = (
                f"**🦹‍♀️ PLUGIN NAME 🦹‍♀️ :** `{plugin_name}` \n{CMD_HELP[plugin_name]}"
            )
        reply_pop_up_alert = help_string
        reply_pop_up_alert += "\n\n**(C) Fire-X ** ".format(plugin_name)
        if len(reply_pop_up_alert) >= 4096:
            crackexy = "`Pasting Your Help Menu.`"
            await event.answer(crackexy, cache_time=0, alert=True)
            out_file = reply_pop_up_alert
            url = "https://del.dog/documents"
            r = requests.post(url, data=out_file.encode("UTF-8")).json()
            url = f"https://del.dog/{r['key']}"
            await event.edit(
                f"Pasted {plugin_name} to {url}",
                link_preview=False,
                buttons=[[custom.Button.inline("Go Back", data="backme")]],
            )
        else:
            await event.edit(
                message=reply_pop_up_alert,
                buttons=[[custom.Button.inline("Go Back", data="backme")]],
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            text = inlinestats
            await event.answer(text, alert=True)
        else:
            txt = "You Can't View My Boss Stats"
            await event.answer(txt, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"yt_dla_(.*)")))
    async def rip(event):
        yt_dl_data = event.data_match.group(1).decode("UTF-8")
        link_s = yt_dl_data
        if event.query.user_id != bot.uid:
            text = f"Please Get Your Own Meow-X And Don't Waste My Resources"
            await event.answer(text, alert=True)
            return
        is_it = True
        await _ytdl(link_s, is_it, event, tgbot)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deezer_dl_(.*)")))
    async def rip(event):
        sun = event.data_match.group(1).decode("UTF-8")

        if event.query.user_id != bot.uid:
            text = f"Please Get Your Own Meow-X And Don't Waste My Resources"
            await event.answer(text, alert=True)
            return
        await _deezer_dl(sun, event, tgbot)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"yt_vid_(.*)")))
    async def rip(event):
        yt_dl_data = event.data_match.group(1).decode("UTF-8")
        link_s = yt_dl_data
        if event.query.user_id != bot.uid:
            text = f"Please Get Your Own Meow-X And Don't Waste My Resources"
            await event.answer(text, alert=True)
            return
        is_it = False
        await _ytdl(link_s, is_it, event, tgbot)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ph_dl_(.*)")))
    async def rip(event):
        link_s = event.pattern_match.group(1)
        if event.query.user_id != bot.uid:
            text = f"Please Get Your Own Meow-X And Don't Waste My Resources."
            await event.answer(text, alert=True)
            return
        await _phdl(link_s, event, tgbot)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dontspamnigga")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            sedok = "Boss, You Don't Need To Use This."
            await event.answer(sedok, cache_time=0, alert=True)
            return
        await event.get_chat()
        him_id = event.query.user_id
        text1 = "ඔයා ඇවිත් තියෙන්නෙ හොඳ දේකට නෙමේ.. ඔයා තෝරපු එක පිළිගන්න බෑ.. ඒක නිසා ඔයාව Block කරනවා"
        await event.edit("ඔයා තෝරපු එක පිළිගන්න බෑ ❌")
        await borg.send_message(event.query.user_id, text1)
        await borg(functions.contacts.BlockRequest(event.query.user_id))
        await borg.send_message(
            LOG_CHAT,
            f"ආයුබෝවන්, මෝඩ  [පකයා](tg://user?id={him_id}) තහන්ම් එකක් තෝරපු නිසා Block කරා",
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"backme")))
    async def sed(event):
        if event.query.user_id != bot.uid:
            sedok = "මොන පිස්සෙක්ද තෝ? උඹටම කියල බොටෙක් හදාගනිම්."
            await event.answer(sedok, cache_time=0, alert=True)
            return
        await event.answer("Back", cache_time=0, alert=False)
        # This Is Copy of Above Code. (C) @SpEcHiDe
        buttons = paginate_help(0, CMD_HELP, "helpme")
        sed = f"""Fire-X Modules Are Listed Here !\n
    For More Help or Support contact {DEFAULTUSER} \nCurrently Loaded Plugins: {len(CMD_LIST)}\nCurrently using Language - Sinhala (Sinhalese)"""
        await event.edit(message=sed, buttons=buttons)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"whattalk")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            sedok = "Boss, You Don't Need To Use This."
            await event.answer(sedok, cache_time=0, alert=True)
            return
        await event.get_chat()
        him_id = event.query.user_id
        await event.edit("ඔයා තෝරපු එක මම පිළිගන්නවා ✔️")
        text2 = "හරි දැන් මගේ අයිතිකාරයා ඔයාට මැසේජ් එකක් දානකන් ටිකක් ඉවසල ඉන්න. \nගොඩාක් ස්තූතී මැසේජ් කරාට."
        await borg.send_message(event.query.user_id, text2)
        await borg.send_message(
            LOG_CHAT,
            message=f"Hello, [අලුත් පොරක්](tg://user?id={him_id}). ඔයා එක්ක කතා කරන්න ඉල්ලනවා.",
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"askme")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            sedok = "මහත්තයෝ, ඔයා මේක පාවිච්චි කරන්න ඕන නෑ"
            await event.answer(sedok, cache_time=0, alert=True)
            return
        await event.get_chat()
        him_id = event.query.user_id
        await event.edit("ඔයා තෝරපු එක මම පිළිගන්නවා ✔️")
        text3 = "හරි දැන් මගේ අයිතිකාරයා ඔයාට මැසේජ් එකක් දානකන් ටිකක් ඉවසල ඉන්න. \nගොඩාක් ස්තූතී මැසේජ් කරාට."
        await borg.send_message(event.query.user_id, text3)
        await borg.send_message(
            LOG_CHAT,
            message=f"Hello, [අලුත් පොරකට](tg://user?id={him_id}). ඔයාගෙන් දෙයක් ඉල්ලන්න තියේලු.",
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit("menu closed")
        else:
            reply_pop_up_alert = "මොන පිස්සෙක්ද තෝ? උඹටම කියල බොටෙක් හදාගනිම්. "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    def paginate_help(page_number, loaded_modules, prefix):
        number_of_rows = 8
        number_of_cols = 2
        helpable_modules = []
        for p in loaded_modules:
            if not p.startswith("_"):
                helpable_modules.append(p)
        helpable_modules = sorted(helpable_modules)
        modules = [
            custom.Button.inline(
                "{} {} {}".format(
                    Config.EMOJI_TO_DISPLAY_IN_HELP, x, Config.EMOJI_TO_DISPLAY_IN_HELP
                ),
                data="us_plugin_{}".format(x),
            )
            for x in helpable_modules
        ]
        pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
        if len(modules) % number_of_cols == 1:
            pairs.append((modules[-1],))
        max_num_pages = ceil(len(pairs) / number_of_rows)
        modulo_page = page_number % max_num_pages
        if len(pairs) > number_of_rows:
            pairs = pairs[
                modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
            ] + [
                (
                    custom.Button.inline(
                        "⏪ Previous", data="{}_prev({})".format(prefix, modulo_page)
                    ),
                    custom.Button.inline("Close", data="close"),
                    custom.Button.inline(
                        "Next ⏩", data="{}_next({})".format(prefix, modulo_page)
                    ),
                )
            ]
        return pairs


else:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Fire-X"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_HELP, "helpme")
            result = builder.article(
                "© Userbot Help",
                text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
            await event.answer([result])
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**Showing Stats For {DEFAULTUSER}'s Fire-X** \nNote --> Only Owner Can Check This \n(C) Fire-X",
                buttons=[
                    [custom.Button.inline("Show Stats ?", data="terminator")],
                    [
                        Button.url(
                            "Repo Here", "https://github.com/TeamEviral/Meow2.0"
                        )
                    ],
                    [Button.url("Join Channel ❤️", "t.me/https://t.me/Murat_30_God")],
                ],
            )
            await event.answer([result])
        elif event.query.user_id == bot.uid and query.startswith("**Hello"):
            result = builder.photo(
                file=WARN_PIC,
                text=query,
                buttons=[
                    [custom.Button.inline("Spamming", data="dontspamnigga")],
                    [
                        custom.Button.inline(
                            "Casual Talk",
                            data="whattalk",
                        )
                    ],
                    [custom.Button.inline("Requesting", data="askme")],
                ],
            )
            await event.answer([result])

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_popp_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_popp_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_HELP, "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if not event.query.user_id == bot.uid:
            sedok = "Who The Fuck Are You? Get Your Own Fire-X ."
            await event.answer(sedok, cache_time=0, alert=True)
            return
        plugin_name = event.data_match.group(1).decode("UTF-8")
        if plugin_name in CMD_HELP:
            help_string = (
                f"**🦹‍♀️ PLUGIN NAME 🦹‍♀️ :** `{plugin_name}` \n{CMD_HELP[plugin_name]}"
            )
        reply_pop_up_alert = help_string
        reply_pop_up_alert += "\n\n**(C) @FIRE_X_CHANNEL** ".format(plugin_name)
        if len(reply_pop_up_alert) >= 4096:
            crackexy = "`Pasting Your Help Menu.`"
            await event.answer(crackexy, cache_time=0, alert=True)
            out_file = reply_pop_up_alert
            url = "https://del.dog/documents"
            r = requests.post(url, data=out_file.encode("UTF-8")).json()
            url = f"https://del.dog/{r['key']}"
            await event.edit(
                f"Pasted {plugin_name} to {url}",
                link_preview=False,
                buttons=[[custom.Button.inline("Go Back", data="backme")]],
            )
        else:
            await event.edit(
                message=reply_pop_up_alert,
                buttons=[[custom.Button.inline("Go Back", data="backme")]],
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            text = inlinestats
            await event.answer(text, alert=True)
        else:
            txt = "You Can't View My Masters Stats"
            await event.answer(txt, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"yt_dla_(.*)")))
    async def rip(event):
        yt_dl_data = event.data_match.group(1).decode("UTF-8")
        link_s = yt_dl_data
        if event.query.user_id != bot.uid:
            text = f"Please Get Your Own Fire-X And Don't Waste My Resources"
            await event.answer(text, alert=True)
            return
        is_it = True
        await _ytdl(link_s, is_it, event, tgbot)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deezer_dl_(.*)")))
    async def rip(event):
        sun = event.data_match.group(1).decode("UTF-8")

        if event.query.user_id != bot.uid:
            text = f"Please Get Your Own Fire-X And Don't Waste My Resources"
            await event.answer(text, alert=True)
            return
        await _deezer_dl(sun, event, tgbot)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"yt_vid_(.*)")))
    async def rip(event):
        yt_dl_data = event.data_match.group(1).decode("UTF-8")
        link_s = yt_dl_data
        if event.query.user_id != bot.uid:
            text = f"Please Get Your Own Fire-X And Don't Waste My Resources"
            await event.answer(text, alert=True)
            return
        is_it = False
        await _ytdl(link_s, is_it, event, tgbot)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ph_dl_(.*)")))
    async def rip(event):
        link_s = event.pattern_match.group(1)
        if event.query.user_id != bot.uid:
            text = f"Please Get Your Own Fire-X And Don't Waste My Resources."
            await event.answer(text, alert=True)
            return
        await _phdl(link_s, event, tgbot)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dontspamnigga")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            sedok = "Master, You Don't Need To Use This."
            await event.answer(sedok, cache_time=0, alert=True)
            return
        await event.get_chat()
        him_id = event.query.user_id
        text1 = "You Have Chosed A Probhited Option. Therefore, You Have Been Blocked"
        await event.edit("Choice Not Accepted ❌")
        await borg.send_message(event.query.user_id, text1)
        await borg(functions.contacts.BlockRequest(event.query.user_id))
        await borg.send_message(
            LOG_CHAT,
            f"Hello, A Noob [Nibba](tg://user?id={him_id}) Selected Probhited Option, Therefore Blocked.",
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"backme")))
    async def sed(event):
        if event.query.user_id != bot.uid:
            sedok = "Who The Fuck Are You? Get Your Own bot."
            await event.answer(sedok, cache_time=0, alert=True)
            return
        await event.answer("Back", cache_time=0, alert=False)
        # This Is Copy of Above Code. (C) @SpEcHiDe
        buttons = paginate_help(0, CMD_HELP, "helpme")
        sed = f"""Fire-X Userbot Modules Are Listed Here !\n
    For More Help or Support contact {DEFAULTUSER} \nCurrently Loaded Plugins: {len(CMD_LIST)}\nCurrently using Language - English (Standard)"""
        await event.edit(message=sed, buttons=buttons)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"whattalk")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            sedok = "Master, You Don't Need To Use This."
            await event.answer(sedok, cache_time=0, alert=True)
            return
        await event.get_chat()
        him_id = event.query.user_id
        await event.edit("Your Choice Accepted ✔️")
        text2 = "Ok. Please Wait Until My Master will Approve you soon. Don't Spam Here Or Try Anything Stupid. \nThank You For Contacting Me."
        await borg.send_message(event.query.user_id, text2)
        await borg.send_message(
            LOG_CHAT,
            message=f"Hello, A [New User](tg://user?id={him_id}). Wants To Talk With You.",
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"askme")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            sedok = "Master, You Don't Need To Use This."
            await event.answer(sedok, cache_time=0, alert=True)
            return
        await event.get_chat()
        him_id = event.query.user_id
        await event.edit("Your choice is Accepted ✔️")
        text3 = "Ok, Wait. My Master will reply you soon. Kindly, Wait."
        await borg.send_message(event.query.user_id, text3)
        await borg.send_message(
            LOG_CHAT,
            message=f"Hello, A [New User](tg://user?id={him_id}). Wants To Ask You Something.",
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit("menu closed")
        else:
            reply_pop_up_alert = "WTF are you Doing.. "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    def paginate_help(page_number, loaded_modules, prefix):
        number_of_rows = 8
        number_of_cols = 4
        helpable_modules = []
        for p in loaded_modules:
            if not p.startswith("_"):
                helpable_modules.append(p)
        helpable_modules = sorted(helpable_modules)
        modules = [
            custom.Button.inline(
                "{} {} {}".format(
                    Config.EMOJI_TO_DISPLAY_IN_HELP, x, Config.EMOJI_TO_DISPLAY_IN_HELP
                ),
                data="us_plugin_{}".format(x),
            )
            for x in helpable_modules
        ]
        pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
        if len(modules) % number_of_cols == 1:
            pairs.append((modules[-1],))
        max_num_pages = ceil(len(pairs) / number_of_rows)
        modulo_page = page_number % max_num_pages
        if len(pairs) > number_of_rows:
            pairs = pairs[
                modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
            ] + [
                (
                    custom.Button.inline(
                        "⏪ Previous", data="{}_prev({})".format(prefix, modulo_page)
                    ),
                    custom.Button.inline("Close", data="close"),
                    custom.Button.inline(
                        "Next ⏩", data="{}_next({})".format(prefix, modulo_page)
                    ),
                )
            ]
        return pairs



