from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])