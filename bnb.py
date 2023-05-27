import time
from telethon import TelegramClient

api_id = '28698295'
api_hash = '0c2dc742b7f12a21371374d4e6cc1780'
phone = '+919021131951'
message = 🎁 Bonus'
username = '@Free_Bnb_Fast_Pay_Bot'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.send_message(username, message)

with client:
    client.loop.run_until_complete(main())
    while True:
        time.sleep(60)
        client.loop.run_until_complete(main())
