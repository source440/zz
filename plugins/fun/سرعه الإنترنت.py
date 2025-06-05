"""
**❃ جميع هذه الامر تستخدم بالأرسال فقط**
❃ `{i}سرعه النت`

   ⌔∮**هاذا الامر يقوم بقياس سرعة الانترنت واستجابة السورس**
"""
from datetime import datetime
from asyncio import sleep
from .. import jmthon_cmd  # تأكد من وجود هذه في سورسك
from .. import eor, jmthon_cmd  # دالة eor المستعملة في سورس يمنثون 

@jmthon_cmd(pattern="سرعه النت$")
async def _(event):
    start = datetime.now()
    event = await eor(event, "⌔∮ **يتم احتساب سرعة الانترنت** ...")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await sleep(1)
    await event.edit(f"**⌯︙سرعة استجابة البوت:**\n`{ms} ms`")