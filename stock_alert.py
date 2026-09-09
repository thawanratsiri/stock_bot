import yfinance as yf
import asyncio
import os
from telegram import Bot

# ดึงข้อมูลจาก Environment Variables ที่เราจะตั้งค่าใน Render
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# ตั้งค่าหุ้น
TICKER = "PTT.BK"
TARGET_PRICE = 35.0

bot = Bot(token=BOT_TOKEN)

async def check_price():
    try:
        # ดึงข้อมูลหุ้น
        stock = yf.Ticker(TICKER)
        # ดึงราคาล่าสุด
        current_price = stock.fast_info['last_price']
        
        print(f"กำลังเช็คราคา {TICKER}... ราคาปัจจุบันคือ: {current_price:.2f}")
        
        # เงื่อนไขแจ้งเตือน
        if current_price <= TARGET_PRICE:
            msg = f"📉 แจ้งเตือน! หุ้น {TICKER} ราคาอยู่ที่ {current_price:.2f} ต่ำกว่าหรือเท่ากับ {TARGET_PRICE} แล้วครับ"
            await bot.send_message(chat_id=CHAT_ID, text=msg)
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

async def main():
    print("บอทเริ่มทำงานแล้ว...")
    while True:
        await check_price()
        # รอ 5 นาที (300 วินาที) แล้วเช็คใหม่
        await asyncio.sleep(300) 

if __name__ == "__main__":
    asyncio.run(main())