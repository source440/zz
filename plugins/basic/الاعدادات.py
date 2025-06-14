"""
❃ `{i}لوك`
    **⌔∮لـ عرض اخر أسطر من عملية التنصيب وعرض سجل العمليات**
    
❃ `{i}اعادة تشغيل`
    **⌔∮لـ اعادة تشغيل سورس يـــمنثون** ( الافضل تستخدمه في مجموعة السجل )
    
❃ `{i}تحديث`
    **⌔∮لـ تحديث سورس يـــمنثون اذا كان هنالك تحديث جديد ولمعرفة التحديثات تابع** @YamenThon
"""


import os
import sys
import time
import asyncio
from yamenthon.helper.git import repo
from yamenthon.helper import check_update, bash, get_client
from .. import jmdB, jmthon_cmd


@jmthon_cmd(pattern="لوك( (.*)|$)")
async def logs_jmthon(event):
    arg = event.pattern_match.group(1).strip()

    file_path = "YamenThon.log"
    if not arg: 
        with open(file_path, "r") as file:
            content = file.read()[-4000:]
        return await event.eor(f"`{content}`")
    elif arg == "تلجراف":
        client = get_client()
        with open(file_path, "r") as file:
            title = "YamenThon Logs"
            page = client.create_page(title=title, content=[file.read()])
        await event.eor(f'[YamenThon Logs]({page["url"]})', link_preview=True)
    await event.eor(file=file_path)


@jmthon_cmd(pattern="اعادة تشغيل$")
async def restart_jmthon(event):
    restart_steps = [
        {"percent": 10, "message": "**⎈ جـاري إعـادة تشغيـل السـورس.. ⎝🌐⎠**", "bar": "▰▱▱▱▱▱▱▱▱"},
        {"percent": 20, "message": "**⎈ جـاري إغلـاق الاتصـالات.. ⎝📡⎠**", "bar": "▰▰▱▱▱▱▱▱▱"},
        {"percent": 30, "message": "**⎈ جـاري حفظ الإعدادات.. ⎝💾**⎠", "bar": "▰▰▰▱▱▱▱▱▱"},
        {"percent": 40, "message": "**⎈ جـاري إيقـاف الوحـدات.. ⎝⚙️⎠**", "bar": "▰▰▰▰▱▱▱▱▱"},
        {"percent": 50, "message": "**⎈ جـاري تحميـل الملفـات.. ⎝📂**⎠", "bar": "▰▰▰▰▰▱▱▱▱"},
        {"percent": 60, "message": "**⎈ جـاري تهيئـة النظـام.. ⎝🔧⎠**", "bar": "▰▰▰▰▰▰▱▱▱"},
        {"percent": 70, "message": "**⎈ جـاري تشغيـل الخدمـات.. ⎝🛠️**⎠", "bar": "▰▰▰▰▰▰▰▱▱"},
        {"percent": 80, "message": "**⎈ جـاري التحقـق من القـواعد.. ⎝📊**⎠", "bar": "▰▰▰▰▰▰▰▰▱"},
        {"percent": 90, "message": "**⎈ جـاري تنشـيط النظـام.. ⎝⚡**⎠", "bar": "▰▰▰▰▰▰▰▰▰"},
        {"percent": 100, "message": "**⎈ تمـت العمليـة بنجـاح! ⎝✅⎠**", "bar": "▰▰▰▰▰▰▰▰▰"}
    ]

    msg = await event.eor("**⎈ بدء إجراءات إعادة التشغيل.. ⎝🌀⎠**")
    
    for step in restart_steps:
        progress_text = (
            f"𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉](t.me/YamenThon) 𓆪\n"
            f"**{step['message']}**\n\n"
            f"⎔ **التقدم:** {step['percent']}%\n"
            f"⎔ **الحالة:** `{step['bar']}`\n\n"
            f"**⎈ الرجـاء الانتظـار..** ⎝⏳⎠"
        )
        await msg.edit(progress_text)
        await asyncio.sleep(0.8)  # زمن الانتظار بين كل خطوة

    # رسالة الإكمال النهائية
    success_msg = (
        f"𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉](t.me/YamenThon) 𓆪\n\n"
        f"**⎈ تم إعـادة تشغيـل السـورس بنجـاح! ⎝🎉⎠**\n\n"
        f"⎔ **الحالة:** `✅ تم التنفيذ بنجاح`\n"
        f"⎔ **الوقت:** `{time.strftime('%H:%M:%S')}`\n\n"
        f"**⎈ يمكنك الآن استخدام السورس بشكل طبيعي** ⎝✨⎠"
    )
    
    await msg.edit(success_msg)
    await asyncio.sleep(3)  # عرض رسالة النجاح لمدة 3 ثواني
    
    # التنفيذ الفعلي لإعادة التشغيل
    os.execl(sys.executable, sys.executable, "-m", "yamenthon")

@jmthon_cmd(pattern="تحديث( (.*)|$)")
async def update_jmthon(e):
    xx = await e.eor("**⌔∮ جار البحث عن تحديثات لسورس يـــمنثون**")
    cmd = e.pattern_match.group(1).strip()
    
    if cmd and ("سريع" in cmd or "خفيف" in cmd):
        await bash("git pull -f")
        await xx.edit("**⌔∮ جار التحديث الخفيف يرجى الأنتظار**")
        os.execl(sys.executable, sys.executable, "-m", "yamenthon")
        return

    # إظهار رسائل التقدم
    await xx.edit("**⌔∮ جاري التحقق من التحديثات...**")
    await asyncio.sleep(1)
    
    remote_url = repo.get_remote_url()
    if remote_url.endswith(".git"):
        remote_url = remote_url[:-4]
    
    m = check_update()
    if not m:
        return await xx.edit(
            f'<strong>سورس يـــمنثون مُحدث بأخر أصدار</strong>',
            parse_mode="html",
            link_preview=False,
        )

    # رسائل التقدم أثناء التحديث
    steps = [
        (10, "**⌔∮ جاري تحميل التحديثات...🌐**\n\n%𝟷𝟶 ▬▭▭▭▭▭▭▭▭▭"),
        (20, "**⌔∮ جاري تحميل التحديثات...🌐**\n\n%𝟸𝟶 ▬▬▭▭▭▭▭▭▭▭"),
        (30, "**⌔∮ جاري تحميل التحديثات...🌐**\n\n%𝟹𝟶 ▬▬▬▭▭▭▭▭▭▭"),
        (40, "**⌔∮ جاري تحميل التحديثات...🌐**\n\n%𝟺𝟶 ▬▬▬▬▭▭▭▭▭▭"),
        (50, "**⌔∮ جاري تطبيق التحديثات...🌐**\n\n%𝟻𝟶 ▬▬▬▬▬▭▭▭▭▭"),
        (60, "**⌔∮ جاري تطبيق التحديثات...🌐**\n\n%𝟼𝟶 ▬▬▬▬▬▬▭▭▭▭"),
        (70, "**⌔∮ جاري تثبيت المتطلبات...🌐**\n\n%𝟽𝟶 ▬▬▬▬▬▬▬▭▭▭"),
        (80, "**⌔∮ جاري تثبيت المتطلبات...🌐**\n\n%𝟾𝟶 ▬▬▬▬▬▬▬▬▭▭"),
        (90, "**⌔∮ جاري الانتهاء من التحديث...🌐**\n\n%𝟿𝟶 ▬▬▬▬▬▬▬▬▬▭"),
        (100, "**⌔∮ تم التحديث بنجاح! جاري إعادة التشغيل...🔄**\n\n%𝟷𝟶𝟶 ▬▬▬▬▬▬▬▬▬▬💯")
    ]

    for percent, message in steps:
        await xx.edit(message)
        await asyncio.sleep(1)

    await update(xx)


async def update(eve):
    await bash(f"git pull && {sys.executable} -m pip install -r requirements.txt")
    await eve.edit("✅ <strong>تم التحديث بنجاح.</strong>", parse_mode="html")
    os.execl(sys.executable, sys.executable, "-m", "yamenthon")
