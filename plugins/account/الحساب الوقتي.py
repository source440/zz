"""

❃ `{i}اسم وقتي`
❃ `{i}تعيين خط الوقت normal`   》𝟙𝟘 
❃ `{i}تعيين خط الوقت bold`      》𝟭𝟬 
❃ `{i}تعيين خط الوقت circle`     》①⓿ 
❃ `{i}تعيين خط الوقت wide`      》１０ 
❃ `{i}تعيين خط الوقت small`     》¹⁰ 
   **⌔∮لـ بدأ وضع الساعة مع اسمك حسابك**

❃ `{i}انهاء اسم وقتي`
   **⌔∮لـ تعطيل ظهور الساعة مع الأسم الخاص بك**

❃ `{i}بايو وقتي`
   **⌔∮لـ بدأ وضع الساعة مع النبذة/البايو الخاص بك**

❃ `{i}انهاء اسم وقتي`
   **⌔∮لـ تعطيل ظهور الوقت مع النبذة الخاصة بك**
"""


import asyncio
import random
import time

from telethon.tl.functions.account import UpdateProfileRequest

from .. import JmdB, jmubot, jmthon_cmd

USERBIO = JmdB.get_key("MYBIO") or "صلى الله على محمد و أهل بيته"
NAME = JmdB.get_key("NAME")

# الخطوط المتاحة
fonts = {
    "normal": "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡:",
    "bold": "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵:",
    "circle": "⓿①②③④⑤⑥⑦⑧⑨:",
    "wide": "０１２３４５６７８９：",
    "small": "⁰¹²³⁴⁵⁶⁷⁸⁹:",
}

def stylize_time(time_str, style="normal"):
    source = "0123456789:"
    target = fonts.get(style, fonts["normal"])
    return "".join(target[source.index(ch)] if ch in source else ch for ch in time_str)

@jmthon_cmd(pattern="اسم وقتي$")
async def autoname(event):
    if JmdB.get_key("AUTONAME"):
        return await event.eor("**⌔∮ الاسم الوقتي شغال بالاصل**")
    JmdB.set_key("AUTONAME", "True")
    await event.eor("**⌔∮ تم بنجاح تشغيل الاسم الوقتي**", time=6)
    while JmdB.get_key("AUTONAME"):
        HM = time.strftime("%I:%M")
        style = JmdB.get_key("TIMEFONT") or "bold"
        name = stylize_time(HM, style)
        await event.client(UpdateProfileRequest(first_name=name))
        await asyncio.sleep(60)

@jmthon_cmd(pattern="بايو وقتي$")
async def autobio(event):
    if JmdB.get_key("AUTOBIO"):
        return await event.eor("**⌔∮ البايو الوقتي شغال بالاصل**")
    JmdB.set_key("AUTOBIO", "True")
    await event.eor("**⌔∮ تم بنجاح تشغيل البايو الوقتي**", time=6)
    BIOS = [
        "الحمد لله رب العالمين",
        "صلى الله على محمد و أهل بيته",
        "أستغفر الله العلي العظيم"
    ]
    while JmdB.get_key("AUTOBIO"):
        BIOMSG = JmdB.get_key("MYBIO") or random.choice(BIOS)
        HM = time.strftime("%I:%M")
        style = JmdB.get_key("TIMEFONT") or "bold"
        time_text = stylize_time(HM, style)
        about = f"{BIOMSG} | {time_text}"
        await event.client(UpdateProfileRequest(about=about))
        await asyncio.sleep(60)

@jmthon_cmd(pattern=r"انهاء ([\s\S]*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if input_str in ["اسم وقتي", "اسم الوقتي", "الاسم الوقتي", "الاسم وقتي"]:
        if JmdB.get_key("AUTONAME"):
            JmdB.del_key("AUTONAME")
            await event.client(UpdateProfileRequest(first_name=NAME))
            return await event.eor("**- تم بنجاح ايقاف الاسم الوقتي**")
        return await event.eor("**- الاسم الوقتي غير شغال اصلا**")
    if input_str in ["بايو وقتي", "البايو الوقتي"]:
        if JmdB.get_key("AUTOBIO"):
            JmdB.del_key("AUTOBIO")
            await event.client(UpdateProfileRequest(about=USERBIO))
            return await event.eor("**- تم بنجاح ايقاف البايو الوقتي**")
        return await event.eor("**- البايو الوقتي غير شغال اصلا**")

@jmthon_cmd(pattern="تعيين خط الوقت (.+)")
async def set_time_font(event):
    style = event.pattern_match.group(1).strip().lower()
    if style not in fonts:
        styles = "، ".join(fonts.keys())
        return await event.eor(f"❌ الخط `{style}` غير مدعوم\nالخطوط المتاحة: {styles}")
    JmdB.set_key("TIMEFONT", style)
    await event.eor(f"✅**⌔∮ تم تعيين خط الوقت إلى**: `{style}`\nارسل الان 》》❃ `.اسم وقتي`")