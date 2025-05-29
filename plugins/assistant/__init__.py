from telethon.tl.types import InputWebDocument

from yamenthon import tgbot
from yamenthon.decorators.asstbot import tgbot_cmd, callback, in_pattern

from .. import Button, inline_pic, inline_mention, up_catbox

AST_PLUGINS = {}

def get_back_button(name):
    return [Button.inline("رجوع", data=f"{name}")]


@in_pattern(owner=True, func=lambda x: not x.text)
async def inline_alive(o):
    TLINK = inline_pic() or "https://graph.org/file/45bd809c97cf4e1666b99.jpg"
    MSG = "• ** سورس يـــمنثون •**"
    WEB0 = InputWebDocument(
        "https://graph.org/file/45bd809c97cf4e1666b99.jpg", 0, "image/jpg", []
    )
    RES = [
        await o.builder.article(
            type="photo",
            text=MSG,
            include_media=True,
            buttons=[
                [
                    Button.url(
                        "قناة السورس", url="https://T.me/YamenThon"
                    ),
                    Button.url("مجموعة المساعدة", url="t.me/YamenThon_Gorop"),
                ],
            ],
            title="سورس يـــمنثون",
            description="𝗬𝘼𝗠ِ𝗘𝙉ِ𝗧𝙃َ𝗢𝙉ِ | يـــمنثون",
            url=TLINK,
            thumb=WEB0,
            content=InputWebDocument(TLINK, 0, "image/jpg", []),
        )
    ]
    await o.answer(
        RES,
        private=True,
        cache_time=300,
        switch_pm="👥 𝗬𝘼𝗠ِ𝗘𝙉ِ𝗧𝙃َ𝗢𝙉ِ",
        switch_pm_param="start",
    )
