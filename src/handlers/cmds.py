from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()


# /start
@router.message(CommandStart())
async def process_start(message: Message) -> None:
    """Обрабатывает /start и приветствует пользователя по его username."""
    username = message.from_user.username
    if not username:
        await message.answer("⚠️ Не смогли обработать ваше имя.")
        return
    await message.answer(f"👋 Привет, {message.from_user.username}. "
                         f"Используй /help для получения инструкций по использованию бота.")


# /help
@router.message(Command("help"))
async def process_help(message: Message) -> None:
    """Обрабатывает /help и отправляет справку пользователю."""
    await message.answer(
        "📖 Как пользоваться ботом:\n\n"
        "1. Сделайте или выберите фотографию клубники.\n"
        "2. Отправьте изображение в чат.\n"
        "3. Бот проанализирует фото и определит состояние клубники.\n\n"
        "📌 Для лучшего результата отправляйте чёткие фотографии, "
        "где клубника хорошо видна."
    )
