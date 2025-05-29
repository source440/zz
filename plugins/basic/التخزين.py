"""
❃ `{i}ايقاف الحفظ`
    **يستخدم هذا بأرساله عند المستخدم في الدردشة الخاصة**
    **⌔∮لـ أيقاف تخزين الرسائل من المستخدم في مجموعة التخزين**

❃ `{i}تشغيل الحفظ`
    **يستخدم هذا بأرساله عند المستخدم في الدردشة الخاصة**
    **⌔∮لـ أرجاع تخزين الرسائل من المستخدم في مجموعة التخزين**

**⌔∮ ملاحظة: سورس يـــمنثون يقوم بحفظ الصور و الفيديوهات و الصوتيات ذاتية التدمير الى مجموعة التخزين بشكل تلقائي وكذلك يقوم بحفظ التاك في كروب التخزين**🧸♥️
"""
import os

from telethon import events
from telethon.errors import (ChatWriteForbiddenError, MediaCaptionTooLongError,
                             MediaEmptyError, MessageTooLongError,
                             PeerIdInvalidError, UserNotParticipantError)
from telethon.tl.custom import Button
from telethon.tl.types import (MessageEntityMention, MessageEntityMentionName,
                               User)
from telethon.utils import get_display_name

from .. import LOGS, tgbot, JmdB, jmdB, jmubot, jmthon_cmd
from database.core.settings import KeySettings


CACHE_SPAM = {}
TAG_EDITS = {}
Logm = KeySettings("LOGUSERS", cast=list)


@jmubot.on(
    events.NewMessage(
        func=lambda e: e.is_private 
        and (e.photo or e.video or e.voice)
        and getattr(e.media, 'ttl_seconds', None) is not None
        and jmdB.get_key("TAG_CHAT")
    )
)
async def secpic(event):
    sender = await event.get_sender()
    username = sender.username
    user_id = sender.id
    TAG_CHAT = jmdB.get_config("TAG_CHAT")
    result = await event.download_media()
    caption = (
        f"**⌔∮ ميديا ذاتية التدمير وصلت لك !**\n: المرسل @{username}\nالايدي : {user_id}"
    )
    await jmubot.send_file(TAG_CHAT, result, caption=caption)


@jmthon_cmd(pattern="ايقاف الحفظ$")
async def _(e):
    if not e.is_private:
        return await e.eor("**⌔∮ يجب أستخدام هذا الامر عند المستخدم في الدردشة الخاصة**", time=3)
    if not Logm.contains(e.chat_id):
        return await e.eor("**⌔∮ لم يتم تفعيل الحفظ على هذا الحساب ليتم ايقافه**", time=3)

    Logm.remove(e.chat_id)
    return await e.eor("**⌔∮ حسنا، من الان سيتم الغاء حفظ الرسائل من هنا في مجموعة التخزين**", time=3)

@jmthon_cmd(pattern="تشغيل الحفظ$")
async def _(e):
    if not e.is_private:
        return await e.eor("**⌔∮ يجب أستخدام هذا الامر عند المستخدم في الدردشة الخاصة**", time=3)
    if Logm.contains(e.chat_id):
        return await e.eor("**⌔∮ تخزين الرسائل من هذه المحادثة شغال اصلا**", time=3)

    Logm.add(e.chat_id)
    return await e.eor("**⌔∮ حسنا، من الان سيتم تخزين الرسائل من هنا في مجموعة التخزين**", time=3)

@jmubot.on(
    events.NewMessage(
        incoming=True,
        func=lambda e: e.is_private and jmdB.get_key("TAG_CHAT")
    ),
)
async def permitpmhandler(event):
    user = await event.get_sender()
    if user.bot or user.is_self or user.verified or Logm.contains(user.id):
        return
    await event.forward_to(jmdB.get_key("TAG_CHAT") or LOG_CHAT)


@jmubot.on(
    events.NewMessage(
        incoming=True,
        func=lambda e: (e.mentioned) and JmdB.get_key("TAG_CHAT"),
    ),
)
async def all_messages_catcher(e):
    x = await e.get_sender()
    if isinstance(x, User) and (x.bot or x.verified):
        return
    LOG_CHAT = JmdB.get_config("LOG_CHAT")
    NEEDTOLOG = JmdB.get_key("TAG_CHAT")
    buttons = await parse_buttons(e)
    try:
        sent = await tgbot.send_message(NEEDTOLOG, e.message, buttons=buttons)
        if TAG_EDITS.get(e.chat_id):
            TAG_EDITS[e.chat_id].update({e.id: {"id": sent.id, "msg": e}})
        else:
            TAG_EDITS.update({e.chat_id: {e.id: {"id": sent.id, "msg": e}}})
#        tag_add(sent.id, e.chat_id, e.id)
    except MediaEmptyError as er:
        LOGS.debug(f"handling {er}.")
        try:
            msg = await tgbot.get_messages(e.chat_id, ids=e.id)
            sent = await tgbot.send_message(NEEDTOLOG, msg, buttons=buttons)
            if TAG_EDITS.get(e.chat_id):
                TAG_EDITS[e.chat_id].update({e.id: {"id": sent.id, "msg": e}})
            else:
                TAG_EDITS.update({e.chat_id: {e.id: {"id": sent.id, "msg": e}}})
#            tag_add(sent.id, e.chat_id, e.id)
        except Exception as me:
            if not isinstance(me, (PeerIdInvalidError, ValueError)):
                LOGS.exception(me)
            if e.photo or e.sticker or e.gif:
                try:
                    media = await e.download_media()
                    sent = await tgbot.send_message(
                        NEEDTOLOG, e.message.text, file=media, buttons=buttons
                    )
                    if TAG_EDITS.get(e.chat_id):
                        TAG_EDITS[e.chat_id].update({e.id: {"id": sent.id, "msg": e}})
                    else:
                        TAG_EDITS.update({e.chat_id: {e.id: {"id": sent.id, "msg": e}}})
                    return os.remove(media)
                except Exception as er:
                    LOGS.exception(er)
            await tgbot.send_message(NEEDTOLOG, "**⌔∮ هذا النوع من الوسائط غير مدعوم**", buttons=buttons)
    except (PeerIdInvalidError, ValueError) as er:
        LOGS.exception(er)
        try:
            CACHE_SPAM[NEEDTOLOG]
        except KeyError:
            await tgbot.send_message(
                JmdB.get_key("LOG_CHAT"), "**⌔∮ ايدي مجموعة التخزين غير صحيح يرجى تعديله**"
            )
            CACHE_SPAM.update({NEEDTOLOG: True})
    except ChatWriteForbiddenError:
        try:
            await tgbot.get_permissions(NEEDTOLOG, "me")
            MSG = "**⌔∮ يرجى التأكد ان بوت المساعدة مشرف في مجموعة التخزين**"
        except UserNotParticipantError:
            MSG = "**⌔∮ يجب عليك أضافتي الى مجموعة التخزين اولا  :)**"
        try:
            CACHE_SPAM[NEEDTOLOG]
        except KeyError:
            await tgbot.send_message(LOG_CHAT, MSG)
            CACHE_SPAM.update({NEEDTOLOG: True})
    except Exception as er:
        LOGS.exception(er)


if JmdB.get_key("TAG_CHAT"):

    @jmubot.on(events.MessageEdited(func=lambda x: not x.out))
    async def upd_edits(event):
        x = event.sender
        if isinstance(x, User) and (x.bot or x.verified):
            return
        if event.chat_id not in TAG_EDITS:
            if event.sender_id == JmdB.get_key("TAG_CHAT"):
                return
            if event.is_private:
                return
            if entities := event.get_entities_text():
                is_self = False
                username = event.client.me.username
                if username:
                    username = username.lower()
                for ent, text in entities:
                    if isinstance(ent, MessageEntityMention):
                        is_self = text[1:].lower() == username
                    elif isinstance(ent, MessageEntityMentionName):
                        is_self = ent.user_id == event.client.me.id
                if is_self:
                    text = f"**#معدلة & #تاك**\n\n{event.text}"
                    try:
                        sent = await tgbot.send_message(
                            JmdB.get_key("TAG_CHAT"),
                            text,
                            buttons=await parse_buttons(event),
                        )
                    except Exception as er:
                        return LOGS.exception(er)
                    if TAG_EDITS.get(event.chat_id):
                        TAG_EDITS[event.chat_id].update({event.id: {"id": sent.id}})
                    else:
                        TAG_EDITS.update({event.chat_id: {event.id: {"id": sent.id}}})
            return
        d_ = TAG_EDITS[event.chat_id]
        if not d_.get(event.id):
            return
        d_ = d_[event.id]
        if d_["msg"].text == event.text:
            return
        msg = None
        if d_.get("count"):
            d_["count"] += 1
        else:
            msg = True
            d_.update({"count": 1})
        if d_["count"] > 10:
            return
        try:
            MSG = await tgbot.get_messages(JmdB.get_key("TAG_CHAT"), ids=d_["id"])
        except Exception as er:
            return LOGS.exception(er)
        TEXT = MSG.text
        if msg:
            TEXT += "\n\n❃ **تم تعديلها الى**"
        strf = event.edit_date.strftime("%H:%M:%S")
        if "\n" not in event.text:
            TEXT += f"\n❃ `{strf}` : {event.text}"
        else:
            TEXT += f"\n❃ `{strf}` :\n-> {event.text}"
        if d_["count"] == 10:
            TEXT += "\n\n**⌔∮ فقط اوب عشر تعديلات ستظهر**"
        try:
            msg = await MSG.edit(TEXT, buttons=await parse_buttons(event))
            d_["msg"] = msg
        except (MessageTooLongError, MediaCaptionTooLongError):
            del TAG_EDITS[event.chat_id][event.id]
        except Exception as er:
            LOGS.exception(er)


async def parse_buttons(event):
    y, x = event.chat, event.sender
    where_n, who_n = get_display_name(y), get_display_name(x)
    where_l = event.message_link
    buttons = [[Button.url(where_n, where_l)]]
    if isinstance(x, User) and x.username:
        try:
            buttons.append(
                [Button.mention(who_n, await tgbot.get_input_entity(x.username))]
            )
        except Exception as er:
            LOGS.exception(er)
            buttons.append([Button.url(who_n, f"t.me/{x.username}")])
    elif getattr(x, "username"):
        buttons.append([Button.url(who_n, f"t.me/{x.username}")])
    else:
        buttons.append([Button.url(who_n, where_l)])
    replied = await event.get_reply_message()
    if replied and replied.out:
        button = Button.url("لقد رد على", replied.message_link)
        if len(who_n) > 7:
            buttons.append([button])
        else:
            buttons[-1].append(button)
    return buttons
