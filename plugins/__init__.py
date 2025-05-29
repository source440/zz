import requests
from telethon.tl import functions, types
from telethon import Button, events

from yamenthon.decorators.command import jmthon_cmd
from yamenthon.decorators.asstbot import in_pattern, tgbot_cmd, callback
from yamenthon.decorators import eor, eod
from yamenthon.core.helper import time_formatter
from yamenthon.helper import inline_mention, fetch, create_quotly, download_yt, get_yt_link, is_url_work, mediainfo
from yamenthon import *


NAME = OWNER_NAME = JmdB.get_key("NAME")
LOG_CHAT = JmdB.get_config("LOG_CHAT")
TAG_CHAT = JmdB.get_config("TAG_CHAT")

DEV_CHAT = [-1002220862939]
DEVLIST = [5571722913]


def inline_pic(get=False):
    INLINE_PIC = JmdB.get_key("INLINE_PIC")
    if (INLINE_PIC is None) or get:
        return "https://i.postimg.cc/rpCmq92k/image.jpg"
    elif INLINE_PIC:
        return INLINE_PIC


def up_catbox(file_path, userhash=None):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "userhash": userhash}

    with open(file_path, "rb") as f:
        files = {"fileToUpload": f}
        response = requests.post(url, data=data, files=files)

        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code} - {response.text}"
