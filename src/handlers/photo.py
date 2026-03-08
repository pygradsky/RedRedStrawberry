from pathlib import Path

from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.photo)
async def process_photo(message: Message) -> None:
    """Сохраняет присланное фото и отправляет подтверждение с размерами."""
    photo = message.photo[-1]

    file_info = await message.bot.get_file(photo.file_id)
    dest = Path("downloads") / str(message.from_user.id) / f"{photo.file_unique_id[:10]}.jpg"
    dest.parent.mkdir(exist_ok=True)

    await message.bot.download_file(file_info.file_path, destination=dest)

    await message.answer(
        f"✅ Готово! Изображение было сохранено\n\n"
        f"• Размер: {photo.width}x{photo.height}\n"
        f"• Файл: {dest.name}"
    )
