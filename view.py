from bot import bot

async def start_game(message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}\n')

async def bot_ask(message, question):
    await bot.send_message(message.from_user.id, f'{question}\n')

async def bot_win(message, word):
    await bot.send_message(message.from_user.id, f'Твоё слово: {word}')

async def next_question(message):
    await bot.send_message(message.from_user.id, 'Следующий вопрос')