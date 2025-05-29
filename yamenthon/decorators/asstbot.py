import inspect
import re
from html import escape
from traceback import format_exc, extract_stack
from pathlib import Path

from telethon import Button
from telethon.errors import QueryIdInvalidError
from telethon.events import CallbackQuery, InlineQuery, NewMessage
from telethon.tl.types import InputWebDocument

from yamenthon import LOGS, tgbot, jmdB, jmubot
from database import InlinePlugin, InlinePaths
from ..helper import make_html_telegraph as mkgraph
from ..helper import admin_check
from . import owner_and_sudos


OWNER = jmubot.full_name
CWD = Path.cwd()

MSG = f"""
**⌔∮ بوت سورس يـــمنثون @YamenThon**
❃ **المالك**: [{OWNER}](tg://user?id={jmubot.uid})
❃ **الـدَعمُ**: @YamenThon
"""



def tgbot_cmd(pattern=None, load=None, owner=False, **kwargs):
    inspect.stack()[1].filename.split("/")[-1].replace(".py", "")
    kwargs["forwards"] = False
    if pattern:
        kwargs["pattern"] = re.compile(f"^/{pattern}")

    def jmt(func):
        async def handler(event):
            if owner and event.sender_id not in owner_and_sudos():
                return
            try:
                await func(event)
            except Exception as er:
                LOGS.exception(er)

        tgbot.add_event_handler(handler, NewMessage(**kwargs))

    return jmt


def callback(data=None, from_users=[], admins=False, owner=False, **kwargs):
    if "me" in from_users:
        from_users.remove("me")
        from_users.append(jmubot.me.id)

    def jmth(func):
        async def wrapper(event):
            if admins and not await admin_check(event):
                return
            if from_users and event.sender_id not in from_users:
                return await event.answer("هذه ليست لك نصب يـــمنثون بنفسك من @YamenThon", alert=True)
            if owner and event.sender_id not in owner_and_sudos():
                return await event.answer(f"هذا هو بوت يـــمنثون الخاص بـ {OWNER} تابعنا @YamenThon")
            try:
                await func(event)
            except Exception as er:
                LOGS.exception(er)

        tgbot.add_event_handler(wrapper, CallbackQuery(data=data, **kwargs))

    return jmth


def in_pattern(pattern=None, owner=False, button=None, **kwargs):
    def don(func):
        async def wrapper(event):
            if owner and event.sender_id not in owner_and_sudos():
                IN_BTTS = [
                    [
                        Button.url(
                            "قناة السورس",
                            url="https://t.me/YamenThon",
                        ),
                        Button.url("مجموعة يـــمنثون", url="https://t.me/YamenThon1"),
                    ]
                ]

                res = [
                    await event.builder.article(
                        title="سورس يـــمنثون",
                        url="https://t.me/YamenThon",
                        description="(c) 𝗬𝘼𝗠ِ𝗘𝙉ِ𝗧𝙃َ𝗢𝙉ِ",
                        text=MSG,
                        thumb=InputWebDocument(
                            "resources/Yemen.jpg",
                            0,
                            "image/jpeg",
                            [],
                        ),
                        buttons=IN_BTTS,
                    )
                ]
                return await event.answer(
                    res,
                    switch_pm=f"🤖: المُساعد لـ {OWNER}",
                    switch_pm_param="start",
                )
            try:
                await func(event)
            except QueryIdInvalidError:
                pass
            except Exception:
                err = format_exc()
                MakeHtml = f"""
البوت: <a href='https://{tgbot.me.username}.t.me'>@{tgbot.me.username}</a>
<h3>العـملية:</h3><br />
<pre>{escape(pattern or '')}</pre><br />
<h3><b>تتبع العملية :</b></h3><br />
<pre>{escape(err)}</pre>
"""
                try:
                    graphLink = await mkgraph("yamenthon Inline Error", MakeHtml)
                except Exception as er:
                    LOGS.exception(f"حدث خطأ اثناء لصق تقرير مشكلة الأنلاين: {er}")
                    LOGS.exception(err)
                    return
                try:
                    await event.answer(
                        [
                            await event.builder.article(
                                title="حدثت مشكلة غير متوقعة",
                                text=graphLink,
                                buttons=Button.url(
                                    "بلغ عنها", "https://t.me/YamenThon1"
                                ),
                            )
                        ]
                    )
                except QueryIdInvalidError:
                    msg = f"<b><a href={graphLink}>[حـدث خـطأ مـا] ⚠️</a></b>"
                    await tgbot.send_message(jmdB.get_config("LOG_CHANNEL"), msg)
                except Exception as er:
                    LOGS.exception(err)
                    LOGS.exception(er)

        tgbot.add_event_handler(wrapper, InlineQuery(pattern=pattern, **kwargs))

    if button:
        InlinePlugin.update(button)
        if kwargs.get("add_help") is not False:
            _path = extract_stack(limit=2)[0].filename[:-3][len(str(CWD)) + 1 :]
            InlinePaths.append(_path.replace("/", "."))
    return don
