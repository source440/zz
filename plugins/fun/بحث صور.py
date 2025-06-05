"""
**❃ جميع هذه الاوامر تستخدم بالأرسال فقط**

❃ `{i}صور`  + محتوى الصور 
    هاذا الامر يقوم بالبحث عن الصـور مثلا اكتب .صور قطط
    
❃ `{i}خلفيات` + محتوى الخلفيات
    هاذا الامر يقوم بالبحث عن خلفيات مثلا اكتب .خلفيات قطط

"""
import asyncio
import os
import shutil
import time
from datetime import datetime

import aiohttp
from telethon.utils import guess_extension
from .. import eor, jmthon_cmd

ZELZAL_APP_ID = "6e65179ed1d879f3d905e28ef8803625"

TMP_DOWNLOAD_DIRECTORY = "./downloads/"
if not os.path.exists(TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(TMP_DOWNLOAD_DIRECTORY)


async def fetch_and_send_images(event, search_query):
    start = datetime.now()
    await eor(event, f"**╮ ❐ جاري البحث عن `{search_query}` ...𓅫╰**")

    download_dir = os.path.join(TMP_DOWNLOAD_DIRECTORY, search_query)
    os.makedirs(download_dir, exist_ok=True)

    input_url = "https://bots.shrimadhavuk.me/search/"
    headers = {"USER-AGENT": "UseTGBot"}
    url_list = []

    try:
        async with aiohttp.ClientSession() as session:
            params = {
                "q": search_query,
                "app_id": ZELZAL_APP_ID,
                "p": "GoogleImages"
            }

            async with session.get(input_url, params=params, headers=headers) as response:
                if response.status != 200:
                    await eor(event, f"**- خطأ في الاتصال بالخادم (رمز {response.status})**")
                    return

                data = await response.json()

                for result in data.get("results", [])[:5]:  # أرسل فقط 5 صور لتفادي الحظر أو الخطأ
                    image_url = result.get("url")
                    if not image_url:
                        continue

                    try:
                        async with session.get(image_url) as img_response:
                            if img_response.status == 200:
                                content_type = img_response.headers.get("Content-Type")
                                ext = guess_extension(content_type) or ".jpg"

                                file_name = f"{time.time()}{ext}"
                                file_path = os.path.join(download_dir, file_name)

                                with open(file_path, "wb") as f:
                                    f.write(await img_response.read())

                                url_list.append(file_path)
                    except Exception:
                        continue

        if not url_list:
            await eor(event, f"**- لم أتمكن من العثور على نتائج لـ `{search_query}`**")
            return

        for file_path in url_list:
            try:
                await event.client.send_file(event.chat_id, file_path, force_document=True)
                await asyncio.sleep(1.5)  # تأخير لتفادي RateLimit
                os.remove(file_path)
            except Exception as e:
                print(f"خطأ أثناء الإرسال: {str(e)}")

        shutil.rmtree(download_dir, ignore_errors=True)

        end = datetime.now()
        ms = (end - start).seconds
        await eor(event, f"**✓ تم العثور على صور لـ `{search_query}` في {ms} ثانية.**", link_preview=False)
        await asyncio.sleep(4)
        await event.delete()

    except Exception as e:
        await eor(event, f"**- حدث خطأ غير متوقع: {str(e)}**")


@jmthon_cmd(pattern="صور (.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    await fetch_and_send_images(event, query)


@jmthon_cmd(pattern="خلفيات (.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    await fetch_and_send_images(event, query)