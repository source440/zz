# plugins/fun/ايدي.py # الاسطوره عاشق الصمت 
""""
**❃ جميع هذه الاوامر تستخدم بالأرسال فقط**

❃ `{i}ايدي`
    **هاذا الامر يستخدم لعرض معلومات المستخدم برد عليه او بالأرسال فقط لعرض معلوماتك**
    
❃ `{i}ا`    
    **هاذا الامر إختصار للامر (ايدي) يعمل نفس الوظيفة**

❃ `{i}صورته`
    **هاذا الامر يستخدم بي الرد على المستخدم لجلب اول صوره لحساب الشخص**
    
❃ `{i}صورته`  + عدد الصور
    **هاذا الامر يستخدم معا العدد لجلب العدد المطلوب لصور حساب الشخص**

❃ `{i}صوته الكل`
    **هاذا الامر يقوم بجلب جميع صور المستخدم**
    
❃ `{i}رابطه`
    **لـ جـلب اسـم الشخـص بشكـل ماركـدون ⦇.رابطه بالـرد او + معـرف/ايـدي الشخص⦈**
"""
import os
import logging
from telethon.tl.types import MessageEntityMentionName
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.messages import GetCommonChatsRequest, GetMessagesRequest

from .. import eor, jmthon_cmd

plugin_category = "العروض"
LOGS = logging.getLogger(__name__)

CUSTOM_ALIVE_TEXT = "•⎚• مـعلومـات المسـتخـدم مـن بـوت يـــمنثون"
CUSTOM_ALIVE_EMOJI = "✦"
CUSTOM_ALIVE_FONT = "⋆─┄─┄─┄─ يـــمنثون ─┄─┄─┄─⋆"


async def get_user_from_event(event, reply_msg=None):
    if reply_msg and reply_msg.sender_id:
        return await event.client.get_entity(reply_msg.sender_id)
    user = event.pattern_match.group(1)
    if user and user.isnumeric():
        user = int(user)
    if not user:
        user = (await event.client.get_me()).id
    if event.message.entities:
        entity = event.message.entities[0]
        if isinstance(entity, MessageEntityMentionName):
            return await event.client.get_entity(entity.user_id)
    return await event.client.get_entity(user)


async def fetch_info(user, event):
    try:
        full = (await event.client(GetFullUserRequest(user.id))).full_user
        bio = full.about.strip() if full.about else "لا يوجد"
    except:
        full = None
        bio = "لا يوجد"

    username = f"@{user.username}" if user.username else "لايـوجـد معـرف"
    name = user.first_name.replace("\u2060", "") if user.first_name else "غير معروف"
    full_name = getattr(full, 'private_forward_name', None) or name
    is_premium = "نعم" if getattr(user, "premium", False) else "لا"

    rotba = "⌁ العضـو 𓅫 ⌁"
    if user.id == 5571722913:
        rotba = "⌁ مطـور السـورس 𓄂𓆃 ⌁"
    elif user.id in (6937025378, 6669024587):
        rotba = "⌁ مطـور مسـاعـد 𐏕⌁"
    elif user.id == (await event.client.get_me()).id:
        rotba = "⌁ مـالك الحساب 𓀫 ⌁"

    try:
        common = await event.client(GetCommonChatsRequest(user.id, 0, 100))
        groups_count = len(common.chats)
    except:
        groups_count = "غير متاح"

    # تقييم التفاعل من عدد الرسائل
    try:
        rmsg = await event.client.get_messages(event.chat_id, limit=0, from_user=user.id)
        total_msgs = rmsg.total
        if total_msgs < 100:
            interaction = "غير متفاعل 🗿"
        elif 200 < total_msgs < 500:
            interaction = "ضعيف 🗿"
        elif 500 < total_msgs < 700:
            interaction = "شد حيلك 🏇"
        elif 700 < total_msgs < 1000:
            interaction = "ماشي الحال 🏄🏻‍♂"
        elif 1000 < total_msgs < 2000:
            interaction = "ملك التفاعل 🎖"
        elif 2000 < total_msgs < 3000:
            interaction = "امبراطور التفاعل 🥇"
        elif 3000 < total_msgs < 4000:
            interaction = "غنبله 💣"
        else:
            interaction = "نار وشرر 🏆"
    except:
        interaction = "غير معروف"

    # تحسين جزء جلب الصورة
    photo = None
    photo_count = "لا يوجد"
    try:
        photo = await event.client.download_profile_photo(
            user.id,
            file=f"temp/{user.id}.jpg",
            download_big=True
        )
        photo_count = "1" if photo else "لا يوجد"
        if not photo:
            photos = await event.client(GetUserPhotosRequest(user.id, 0, 0, 1))
            if photos and photos.photos:
                photo = await event.client.download_media(photos.photos[0], f"temp/{user.id}_alt.jpg")
                photo_count = str(len(photos.photos))
    except Exception as e:
        LOGS.error(f"Error getting user photo: {str(e)}")
        photo = None
        photo_count = "لا يوجد"

    caption = (
        f"<b> {CUSTOM_ALIVE_TEXT} </b>\n"
        f"ٴ<b> {CUSTOM_ALIVE_FONT} </b>\n"
        f"<b> {CUSTOM_ALIVE_EMOJI} الاسـم ⇠ </b> <a href='tg://user?id={user.id}'>{full_name}</a>\n"
        f"<b> {CUSTOM_ALIVE_EMOJI} المعـرف ⇠ {username}</b>\n"
        f"<b> {CUSTOM_ALIVE_EMOJI} الايـدي ⇠ </b> <code>{user.id}</code>\n"
        f"<b> {CUSTOM_ALIVE_EMOJI} الرتبـــه ⇠ {rotba}</b>\n"
        f"<b> {CUSTOM_ALIVE_EMOJI} الحـساب بريميوم ⇠ {is_premium}</b>\n"
        f"<b> {CUSTOM_ALIVE_EMOJI} المجموعات المشتركة ⇠ {groups_count}</b>\n"
        f"<b> {CUSTOM_ALIVE_EMOJI} الصـور ⇠ {photo_count}</b>\n"
        f"<b> {CUSTOM_ALIVE_EMOJI} البايـو ⇠ {bio}</b>\n"
        f"<b> {CUSTOM_ALIVE_EMOJI} التفاعل ⇠ {interaction}</b>\n"
        f"ٴ<b> {CUSTOM_ALIVE_FONT} </b>"
    )

    return photo, caption


@jmthon_cmd(pattern=r"ايدي(?: |$)(.*)", command=("ايدي", plugin_category))
async def id_info(event):
    reply_msg = await event.get_reply_message()
    z = await eor(event, "⇆")

    user = await get_user_from_event(event, reply_msg)
    if not user:
        return await eor(z, "**لم أستطع العثور على المستخدم**")

    try:
        photo, caption = await fetch_info(user, event)
        reply_id = event.reply_to_msg_id or None

        if photo and os.path.exists(photo):
            try:
                await event.client.send_file(
                    event.chat_id,
                    photo,
                    caption=caption,
                    reply_to=reply_id,
                    parse_mode="html"
                )
            finally:
                try:
                    os.remove(photo)
                except:
                    pass
        else:
            await event.client.send_message(
                event.chat_id,
                caption,
                reply_to=reply_id,
                parse_mode="html"
            )
        await z.delete()
    except Exception as e:
        LOGS.error(f"خطأ في id_info: {str(e)}")
        await eor(z, "**حصل خطأ أثناء جلب المعلومات**")


@jmthon_cmd(pattern=r"ا(?: |$)(.*)", command=("ا", plugin_category))
async def id_info_short(event):
    await id_info(event)


@jmthon_cmd(pattern=r"رابطه(?:\s|$)([\s\S]*)", command=("رابطه", plugin_category))
async def tag_user(event):
    user = await get_user_from_event(event, await event.get_reply_message())
    if not user:
        return
    name = user.first_name.replace("\u2060", "") if user.first_name else user.username
    custom = event.pattern_match.group(1) or name
    await eor(event, f"[{custom}](tg://user?id={user.id})")


@jmthon_cmd(pattern=r"صورته(?:\s|$)([\s\S]*)", command=("صورته", plugin_category))
async def user_photos(event):
    z = await eor(event, "⇆")
    args = event.pattern_match.group(1).strip()
    msg = await event.get_reply_message()
    user = msg.sender if msg else await event.client.get_entity(event.input_chat)
    photos = await event.client.get_profile_photos(user)

    if args.lower() == "الكل":
        if photos:
            await event.client.send_file(event.chat_id, photos)
        else:
            await eor(z, "**لا توجد صور للمستخدم**")
    else:
        try:
            index = int(args) if args else 1
            if index <= 0 or index > len(photos):
                return await eor(z, "**رقم غير صالح أو لا توجد صور بهذا الرقم**")
            photo = await event.client.download_media(photos[index - 1])
            await event.client.send_file(event.chat_id, photo)
            os.remove(photo)
        except:
            await eor(z, "**حدث خطأ أثناء جلب الصورة**")
    await z.delete()