from aiogram import types

import bot
from generic import Gen
from source import Word
import main
import model, view
from database import DATABASE

all_users = {
}



async def start_game(message: types.Message):
    global all_users
    tgid = message.from_user.id
    wordDatabase, wordDataGraph = main.fill([], main.DataGraph())
    g = Gen()
    g.addSign("Живое")

    all_users[tgid] = {
        'gen': g,
        'wordDatabase': wordDatabase,
        'wordDataGraph':  wordDataGraph,
        'currentNode': 'Живое',
        }

    return await bot.bot.send_message(message.chat.id, 'живое?')


async def player_turn(message: types.Message):
    tgid = message.from_user.id
    gen = all_users[tgid]['gen']
    wordDatabase = all_users[tgid]['wordDatabase']
    wordDataGraph = all_users[tgid]['wordDataGraph']
    currentNode = all_users[tgid]['currentNode']

    probWord = main.findHyphothesis(gen, wordDatabase)
    ans = message.text

    match ans:
        case "yes":
            currentNode = main.findHyphSign(probWord.value, currentNode)
            gen.addSign(currentNode)
            probWord = main.findHyphothesis(gen, wordDatabase)
        case "no":
            side = wordDataGraph.getSideNeighbours(main.findHyphSign(probWord.value, currentNode))
            probWord = main.findHyphFromSides(gen, side, wordDatabase)
            gen.addSign(main.findHyphSign(probWord.value, currentNode))

    all_users[tgid] = {
        'currentNode': currentNode,
        'gen': gen,
        'wordDatabase': wordDatabase,
        'wordDataGraph': wordDataGraph
    }


    if ans in ["yes",  "no"]:
        if max(gen.fitness) > 0.8:
            return await bot.bot.send_message(message.chat.id, probWord.value)
        else:
           await bot.bot.send_message(message.chat.id, str(main.findHyphSign(probWord.value, currentNode)) + '?')
