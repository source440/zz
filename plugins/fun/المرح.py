"""
**❃ جميع هذه الاوامر تستخدم بالرد على الشخص عدا أمر كت**

❃ `{i}رفع مطي`
❃ `{i}رفع كلب`
❃ `{i}رفع حيوان`
❃ `{i}رفع زاحف`
❃ `{i}رفع مرتي`
❃ `{i}رفع زوجي`
❃ `{i}رفع تاج`
❃ `{i}رفع بقلبي`
❃ `{i}رفع بزون`
❃ `{i}رفع قرد`

❃ `{i}نسبة الحب`
❃ `{i}نسبة الانوثة`
❃ `{i}نسبة الرجولة`
❃ `{i}نسبة الغباء`
❃ `{i}نسبة المثلية`

❃ `{i}كت`
❃ `{i}اوصف`
❃ `{i}هينه`
❃ `{i}نزوج`
❃ `{i}طلاق`
"""

import random

from yamenthon.helper import get_uinfo
from resources.fun import *

from .. import *

@jmthon_cmd(pattern="رفع بقلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if custom:
        return await eor(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بقلبك 🥺🖤 ")

@jmthon_cmd(pattern="رفع زوجي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if custom:
        return await eor(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعه زوجج روحوا خلفوا 🤤😂")

@jmthon_cmd(pattern="رفع مطي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6669024587:
        return await eor(mention, f"**⌔∮ أبتعد هذا صديق المطور لا**")
    if user.id == 5571722913:
        return await eor(mention, f"**⌔∮ احترم نفسك هاذا مطوري يا تعبان **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفـعه مطي هـنا ")

@jmthon_cmd(pattern="رفع مرتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6669024587:
        return await eor(mention, f"**⌔∮ أبتعد هذا صديق المطور لا**")
    if user.id == 5571722913:
        return await eor(mention, f"**- احترم نفسك هاذا مطوري يا تعبان **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤")

@jmthon_cmd(pattern="رفع كلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6669024587:
        return await eor(mention, f"**⌔∮ أبتعد هذا صديق المطور لا**")
    if user.id == 5571722913:
        return await eor(mention, f"**- احترم نفسك هاذا مطوري يا تعبان **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه كلب خليه خله ينبح 😂🐶")

@jmthon_cmd(pattern="كت(?: |$)(.*)")
async def mention(mention):
    kt = random.choice(kattwet)
    await eor(mention, f"**- {kt}**")

@jmthon_cmd(pattern="هينه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6669024587:
        return await eor(mention, f"**⌔∮ أبتعد هذا صديق المطور لا**")
    if user.id == 5571722913:
        return await eor(mention, f"**- احترم نفسك هاذا مطوري يا تعبان **")
    sos = random.choice(hena)
    await eor(mention, f"{sos} .")

@jmthon_cmd(pattern="نسبة الحب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    moh = random.choice(nsba)
    await eor(mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {moh} 😔🖤")

@jmthon_cmd(pattern="نسبة الانوثة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6669024587:
        return await eor(mention, f"**⌔∮ أبتعد هذا صديق المطور لا**")
    if user.id == 5571722913:
        return await eor(mention, f"**- لكك دي هذا المطور رجال وعلى راسك**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await eor(mention, f"- نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هي {sos} 🥵🖤")

@jmthon_cmd(pattern="نسبة الغباء(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 5571722913:
        return await eor(mention, f"**- برد لك بس ذا مطور السورس يا ورع 😂**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    jmbot = random.choice(rr7)
    await eor(mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {jmbot} 😂💔")

@jmthon_cmd(pattern="رفع تاج(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if custom:
        return await eor(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه تاج 👑🔥")

@jmthon_cmd(pattern="رفع قرد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6669024587:
        return await eor(mention, f"**⌔∮ أبتعد هذا صديق المطور لا**")
    if user.id == 5571722913:
        return await eor(mention, f"**- احترم نفسك هاذا مطوري يا فتال**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه قرد واعطائه موزة 🐒🍌")

@jmthon_cmd(pattern="اوصف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    jmbot = random.choice(Describe)
    await eor(mention, f"{jmbot}")

@jmthon_cmd(pattern="شغله(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    rezw = random.choice(jobtype)
    await eor(mention, f"- المستخدم [{user.first_name}](tg://user?id={user.id}) شغله هو {rezw}")

@jmthon_cmd(pattern="نسبة الرجولة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6669024587:
        return await eor(mention, f"**⌔∮ نسبة رجولة مساعد المطور هي 99%**")
    if user.id == 5571722913:
        return await eor(mention, f"**⌔∮ نسبة رجولة الاسطوره عاشق الصمت مالك السورس هي 100%**")
    sos = random.choice(kz)
    await eor(mention, f"- نسبة الرجولة لـ [{user.first_name}](tg://user?id={user.id}) هـي {sos} 🥵🖤")

@jmthon_cmd(pattern="رفع حيوان(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 5571722913:
        return await eor(mention, "**⌔∮ عذرا هذا مطوري ياخجف لا يمكنني استخدام الأمر عليه 😂**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه حيوان 🐏")

@jmthon_cmd(pattern="رفع بزون(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 5571722913:
        return await eor(mention, "**⌔∮ عذرا هذا مطوري ياخجف لا يمكنني استخدام الأمر عليه 😂**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بزون 🐈")

@jmthon_cmd(pattern="رفع زاحف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 5571722913:
        return await eor(mention, "**⌔∮ عذرا هذا مطوري ياخجف لا يمكنني استخدام الأمر عليه 😂**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه زاحف 🐍💞")

@jmthon_cmd(pattern="نزوج(?: |$)(.*)")
async def wiffun(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 5571722913:
        return await eor(mention, f"**⌔∮ عذرا هذا مطور السورس**")
    await eor(mention, f"**نزوج وماتشوف على غيري 🥺💞 ܰ**")

@jmthon_cmd(pattern="طلاق(?: |$)(.*)")
async def mention(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 5571722913:
        return await eor(mention, f"**⌔∮ عذرا هذا مطور السورس هو الي يحق له يطلقك ي حلوه 💋😂**")
    await eor(mention, f"**طالق طالق بالعشرة 😹😭💕 ܰ**")
