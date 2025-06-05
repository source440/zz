"""
**❃ جميع هذه الاوامر تستخدم بالأرسال فقط**

❃ `{i}حساب العمر`  +سنة الميلاد 
  
  يستخدم الامر معا سنة الميلاد لحساب العمر
"""



from datetime import datetime
from .. import eor, jmthon_cmd

@jmthon_cmd(pattern=r"حساب العمر(?:\s|$)([\s\S]*)")
async def _(event):
    text = event.text[12:]
    if not text:
        await eor(event, "**✾╎استخـدم الامـر كالتالـي .. حساب العمر + السنـه**")
        return
    try:
        year = int(text.strip())
        age = datetime.now().year - year
        await eor(event, f"**🚹╎عمرك هـو :** {age}")
    except ValueError:
        await eor(event, "**✾╎رجاءً ادخل سنة صحيحة مثل: 2005**")