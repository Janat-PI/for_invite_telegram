from typing import TypedDict

from environs import Env


env = Env()
env.read_env(".env")


class TelegramSettings(TypedDict):

    API_ID: int
    API_HASH: str
    BOT_TOKEN: str
  

tokens = TelegramSettings(
    API_HASH=env("API_HASH"),
    API_ID=env.int("API_ID"),
    BOT_TOKEN= env("BOT_TOKEN")
)
