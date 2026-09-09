import asyncio
from telegram import Bot

# ใส่ข้อมูลของคุณที่นี่
BOT_TOKEN = "8635907285:AAG0-iYsk7xR3pt0U61LkOTfZdrSosvaFlE"
CHAT_ID = "8394123709"

async def send_test():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="สวัสดีครับ! บอททำงานได้แล้ว")
    print("ส่งข้อความทดสอบสำเร็จ!")

if __name__ == "__main__":
    asyncio.run(send_test())