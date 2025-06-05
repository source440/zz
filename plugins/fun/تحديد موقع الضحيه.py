"""
**❃ هاذا الامر تستخدم بالأرسال فقط**

❃ `{i}بحث ايبي`  + ايبي هاتف الضحيه 
   ⌔∮**يستخدم هاذا الامر لتحديد موقع الضحيه من خلال الايبي** 
   **المعلومات قد لا تكون دقيقة** 📵
"""

import asyncio
import json
from urllib.request import urlopen

from .. import jmthon_cmd  # تأكد من وجوده في سورسك
from .. import eor, jmthon_cmd  # يستخدم لتعديل الرسالة بسلاسة

@jmthon_cmd(pattern="بحث ايبي (.+)")
async def _(event):
    ip = event.pattern_match.group(1)
    event = await eor(event, "⌔∮ يتم البحث عن معلومات الـ IP ...")
    await asyncio.sleep(2)

    try:
        url = f"http://ip-api.com/json/{ip}"
        response = urlopen(url)
        data = json.loads(response.read())

        if data["status"] == "fail":
            await event.edit(f"⚠️ لم يتم العثور على IP: `{ip}`")
            return

        result = f"""⌯︙معلومات حول: `{data['query']}`
الدولة: {data['country']}
كود الدولة: {data['countryCode']}
المنطقة: {data['region']} - {data['regionName']}
المدينة: {data['city']}
الرمز البريدي: {data['zip']}
خط العرض: {data['lat']}
خط الطول: {data['lon']}
المنطقة الزمنية: {data['timezone']}
شركة الاتصال: {data['isp'].title()}
المنظمة: {data['org'].title()}
ASN: {data['as']}
"""
        await event.edit(result)

    except Exception as e:
        await event.edit(f"⚠️ حدث خطأ أثناء البحث:\n`{str(e)}`")