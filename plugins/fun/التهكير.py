"""
❃ `{i}تهكير`<بالرد على المستخدم>
    امر ترفيهي للمزاح مع صديقك بانك قمت ب اختراقه
"""

import asyncio
from .. import OWNER_NAME, jmthon_cmd


async def run_animation(event, steps, interval=2):
    for step in steps:
        await asyncio.sleep(interval)
        await event.edit(step)

@jmthon_cmd(pattern="تهكير$")
async def _(event):
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        idd = reply_message.sender_id
        if idd == 5571722913:
            await event.eor("**⌔∮ عذرا هذا مطوري ياخجف لا يمكنني استخدام الأمر عليه 😂**")
        else:
            steps = [
                "⚙️ جاري إنشاء الاتصال بالخادم...",
                "🔍 تم تحديد الهدف: يتم جمع البيانات الأولية...",
                "📡 الاتصال بالمخدمات السرية جارٍ... 10%",
                "📂 استخراج المعلومات السرية... 35%",
                "💾 يتم تنزيل الملفات المحمية... 60%",
                "🔓 فك تشفير البيانات... 85%",
                "✅ تم الوصول الكامل! 💥",
                "جار الاختراق... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 84%\n█████████████████████▒▒▒▒ ",
                "جار الاختراق... 100%\n████████████████████████ ",
                f"📁 جميع ملفاتك الآن في يدي! 😈\n⚠️ لتجنب نشر بياناتك، أرسل 1,000,000$ الآن! 😂"
            ]
            await run_animation(event, steps)
    else:
        await event.eor("**⌔∮ يرجى الرد على المستخدم أولاً**")

        
@jmthon_cmd(pattern="تهكير2$")
async def _(event):
    steps = [
        "**يتم الربط بقاعدة بيانات التليجرام**",
        f"تم تحديد الضحية من قبل: {OWNER_NAME}",
        "جار الاختراق... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
        "جار الاختراق... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
        "جار الاختراق... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
        "جار الاختراق... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
        "جار الاختراق... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
        "جار الاختراق... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
        "جار الاختراق... 84%\n█████████████████████▒▒▒▒ ",
        "جار الاختراق... 100%\n█████████تم الاختراق ███████████ ",
        f"**تم بنجاح اختراق قاعدة بيانات التليجرام\n\nادفع 699$ إلى {OWNER_NAME} لحذف ملفات الاختراق**"
    ]
    await run_animation(event, steps)

@jmthon_cmd(pattern="تهكير3$")
async def _(event):
    steps = [
        "- يتم البحث عن قاعدة بيانات المستخدم...",
        "حالة المستخدم: متصل\nصلاحيات التليجرام: موجودة\nخصوصية التخزين: موجودة",
        "جار الاختراق... 0%\n[░░░░░░░░░░░░░░░░░░░░]\nيتم البحث عن المعلومات...\nETA: 0m, 30s",
        "جار الاختراق... 20.63%\n[███░░░░░░░░░░░░░░░░░]\nتم إيجاد الملف\nC:/WhatsApp\nETA: 0m, 24s",
        "جار الاختراق... 55.30%\n[█████████░░░░░░░░░░░]\nmsgstore.db.crypt12\nETA: 0m, 15s",
        "جار الاختراق... 74.02%\n[█████████████░░░░░░░]\nيتم فك التشفير...\nETA: 0m, 09s",
        "جار الاختراق... 100%\n[████████████████████]\nتم فك التشفير بنجاح!",
        "- حساب الضحية تم اختراقه بنجاح!\n\n✅ جميع بياناته تم رفعها إلى السيرفر."
    ]
    await run_animation(event, steps)
