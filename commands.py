from aiogram import types

import bot
import main
import model, view
from database import DATABASE

async def start_game(message: types.Message):
    await model.set_game()
    await view.start_game(message)
    name = message.from_user.first_name
    await model.set_player_name(name)

    # Бот спрашивет
    if model.steps_amount == 0:
        await view.bot_ask(message, "Живое?")
    else:
        await view.bot_ask(message, str(main.findHyphSign(model.probword.value, model.current_node) + '?'))

    # Человек отвечает
    model.answer = 'test'
    await player_turn(message)
    # Бот ходит, т.е. обрабатывает
    print("testing")
    if (model.answer != 'test'):
        await bot_turn(message)

async def bot_turn(message: types.Message):
    # ЗДЕСЬ БОТ ОБРАБАТЫВАЕТ ОТВЕТ ПОЛЬЗОВАТЕЛЯ в game()

    match model.answer:
        case 'yes':
            if (model.steps_amount == 0):
                model.current_node = 'Живое'
            else:
                model.current_node = model.next_node
            model.total_gen.addSign(model.current_node)
            model.probword = main.findHyphothesis(model.total_gen, main.wordDatabase)
        case 'no':
            if (model.steps_amount == 0):
                model.current_node = 'Неживое'
                model.total_gen.addSign(model.current_node)
            else:
                sides = main.wordDataGraph.getSideNeighbours(main.findHyphSign(model.probword.value, model.current_node))
                model.probword = main.findHyphFromSides(model.total_gen, sides, main.wordDatabase)
                model.total_gen.addSign(main.findHyphSign(model.probword.value, model.current_node))

    #await model.set_total_word(model.current_node)
    #name = await model.get_player_name()
    #total_word = await model.get_total_word()

    if (model.current_node not in DATABASE):
        await bot.bot.send_message(message.chat.id, "test123")
    if (model.current_node in DATABASE):
        await view.bot_win(message, model.current_node)
        await model.set_game()


async def player_turn(message: types.Message):
    game = await model.get_game()

    if (game):
        if message.text == '/game':
            return
        else:
            model.answer = message.text

    await bot_turn(message)