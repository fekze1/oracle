from aiogram.utils import executor
import handlers
import main
from bot import dp


async def on_startup(_):
    print('Бот запущен')

handlers.register_handlers(dp)

main.fill()

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)