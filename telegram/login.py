from typing import Any

from telethon import TelegramClient, events
from environs import Env

from excel_read.classes import User


env = Env()
env.read_env(".env")

API_ID = env.int("API_ID")
API_HASH = env("API_HASH")


class Login:

    def sign_in(self, *args, **kwargs):

        with TelegramClient("session_1", API_ID, API_HASH) as client:
            client: TelegramClient

            @client.on(events.NewMessage(pattern='(?i).*Hello'))
            async def handler(event):
                await event.reply('Hey!')
                print(kwargs)
                await client.send_message("me", message=str(kwargs["user"]))

            client.run_until_disconnected()


    def get_clients(self, all_clients: list[User]) -> list[User]:
        return all_clients[0]

        
