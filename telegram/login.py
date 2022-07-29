from typing import Any

from telethon.sync import TelegramClient
from telethon import TelegramClient, events

from telethon.tl.types import PeerUser


from excel_read.classes import User


class Client():

    def __init__(self,API_ID, API_HASH, BOT_TOKEN: str | None = None) -> None:
        self._API_ID = API_ID
        self._API_HASH = API_HASH
        self._BOT_TOKEN = BOT_TOKEN
        # self._client = TelegramClient("session_1", API_ID, API_HASH).start(
        #     bot_token=BOT_TOKEN if BOT_TOKEN else "996709855133"
        # )
        self._client = TelegramClient("session_1", API_ID, API_HASH)

    @property
    def get_client(self) -> TelegramClient:
        return self._client

    # def sign_in(self, *args, **kwargs):

    #     with TelegramClient("session_1", API_ID, API_HASH) as client:
    #         client: TelegramClient

    #         @client.on(events.NewMessage(pattern='(?i).*Hello'))
    #         async def handler(event):
    #             await event.reply('Hey!')
    #             print(kwargs)
    #             await client.send_message("me", message=str(kwargs["user"]))

    #         client.run_until_disconnected()


    async def about_me(self, *args, **kwargs):
        me = await self._client.get_me()
        # print(me.stringify())

        # some_client = await self.get_clients(kwargs.get("all_clients"))
        # print(some_client)

        try:
            answer = await self._client.get_peer_id("+996705192362")
        except ValueError:
            print("she's not register on telegram")
        else:
            print(answer)


        # for client in some_client:
        #     client: User
        #     if client.phone.startswith("0"):
        #         client.phone = "996" + client.phone[1:]
        #     try:
        #         await self._client.send_message(client.phone, message="it's new test")
        #     except ValueError:
        #         print(client.name + "  not in telegram")
        #     else:
        #         print(client.name + " all okey!!!!!! he/she's in telegram!!!!!")

        # answer = await self._client.get_entity("me")
        # print(answer)
        
        # await self._client.send_message(e, message="hi")
        

    async def get_clients(self, all_clients: list[User]) -> list[User] | User:
        return all_clients[30:100]

        
