#    Copyright (C) 2020  sandeep.n(π.$)
# button post makker for catuserbot thanks to uniborg for the base

# Translate to arabic by @JMTHON  - @RRRD7
import os
import re

from telethon import Button

from ..Config import Config
from . import catub, edit_delete, reply_id

plugin_category = "tools"
# regex obtained from:
# https://github.com/PaulSonOfLars/tgbot/blob/master/tg_bot/modules/helper_funcs/string_handling.py#L23


@catub.cat_cmd(
    pattern="لستة(?: |$)(.*)",
    command=("لستة", plugin_category),
    info={
        "header": "To create button posts via inline",
        "note": f"Markdown is Default to html",
        "options": "If you button to be in same row as other button then follow this <buttonurl:link:same> in 2nd button.",
        "usage": [
            "{tr}ibutton <text> [Name on button]<buttonurl:link you want to open>",
        ],
        "examples": "{tr}لستة قنواتي الرسمية [𝗧ُِٔ𝗢ٍَِ𝗢َِّ𝗟َٖ𝗦َ]<buttonurl:t.me/JMTHON> [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ]<buttonurl:t.me/JMTHON> ",
    },
)
async def _(event):
    "To create button posts via inline"
    reply_to_id = await reply_id(event)
    # soon will try to add media support
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(event, "** يجب عليك وضع متابه لاستخدامها مع الامر **")
    catinput = "Inline buttons " + markdown_note
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, catinput)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb
