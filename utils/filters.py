from pyrogram import Client, filters
from pyrogram.types import Message

from core.config import bs


async def _is_admin(_: object, __: Client, msg: Message) -> bool:
    return msg.from_user is not None and msg.from_user.id in bs.admins


is_admin = filters.create(_is_admin)
