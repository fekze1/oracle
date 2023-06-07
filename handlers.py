from aiogram import Dispatcher
import commands

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_game, commands=['game'])
    dp.register_message_handler(commands.player_turn)