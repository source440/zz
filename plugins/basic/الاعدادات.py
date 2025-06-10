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
    await event.eor("**⌔∮ جار اعادة تشغيل سورس يـــمنثون سيتم تنبيهك في مجموعة السجل; بعد تشغيل السورس أنتظر فقط ▬▭ ...**🧸♥️")
    os.execl(sys.executable, sys.executable, "-m", "yamenthon")

@jmthon_cmd(pattern="تحديث( (.*)|$)")
async def update_jmthon(e):
    xx = await e.eor("**⌔∮ جار البحث عن تحديثات لسورس يـــمنثون**")
    cmd = e.pattern_match.group(1).strip()
    if cmd and ("سريع" in cmd or "خفيف" in cmd):
        await bash("git pull -f")
        await xx.edit("**⌔∮ جار التحديث الخفيف يرجى الأنتظار**")
        os.execl(sys.executable, sys.executable, "-m", "yamenthon")

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

    msg = await xx.eor(
        f'<strong>جـار تحديث سورس يـــمنثون يرجى الأنتظار قليلا</strong>',
        parse_mode="html",
        link_preview=False,
    )
    await update(msg)


async def update(eve):
    await bash(f"git pull && {sys.executable} -m pip install -r requirements.txt")
    await eve.edit("✅ <strong>تم التحديث بنجاح.</strong>", parse_mode="html")
    os.execl(sys.executable, sys.executable, "-m", "yamenthon")
