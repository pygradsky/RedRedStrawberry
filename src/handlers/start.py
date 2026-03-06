from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def process_start(message: Message):
    username = message.from_user.username
    if not username:
        await message.answer(
            "⚠️ We could not process your name."
        )
        return
    await message.answer(
        f"👋 Hello, {message.from_user.username}"
    )
