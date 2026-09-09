import yfinance as yf
import asyncio
import time
from telegram import Bot

# ตั้งค่าข้อมูลของคุณ
BOT_TOKEN = "8635907285:AAG0-iYsk7xR3pt0U61LkOTfZdrSosvaFlE"
CHAT_ID = "8394123709"
TICKER = "PTT.BK"       # ตัวอย่างหุ้นไทย PTT
TARGET_PRICE = 40.0      # ราคาที่ต้องการแจ้งเตือน

bot = Bot(token=BOT_TOKEN)

async def check_price():
    # ดึงข้อมูลหุ้น
    stock = yf.Ticker(TICKER)
    # ดึงราคาล่าสุด (market price)
    current_price = stock.fast_info['last_price']
    
    print(f"กำลังเช็คราคา {TICKER}... ราคาปัจจุบันคือ: {current_price:.2f}")
    
    # เงื่อนไขแจ้งเตือน (กรณีราคาต่ำกว่าหรือเท่ากับที่กำหนด)
        # เปลี่ยนเงื่อนไขเป็น > เพื่อให้บอทแจ้งเตือนได้ทันทีหากราคามากกว่า 0 (ซึ่งเป็นไปได้จริง)
    if current_price > 0: 
        msg = f"✅ ทดสอบ: หุ้น {TICKER} ราคาปัจจุบันคือ {current_price:.2f} บาท"
        await bot.send_message(chat_id=CHAT_ID, text=msg)

async def main():
    while True:
        try:
            await check_price()
        except Exception as e:
            print(f"Error: {e}")
        # รอ 5 นาที (300 วินาที) แล้วเช็คใหม่
        await asyncio.sleep(300)
        
if __name__ == "__main__":
    asyncio.run(check_price())