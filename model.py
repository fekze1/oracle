import generic

game = False
player_name = ''
total_word = 'START'
total_gen = generic.Gen()
steps_amount = 0
current_node = ''
next_node = ''
probword = ''
answer = ''

async def set_game():
    global game, player_name, total_word, total_gen, steps_amount, current_node, next_node, probword, answer

    if (game == False):
        game = True
    else:
        player_name = ''
        total_word = 'START'
        current_node = ''
        next_node = ''
        answer = ''
        probword = ''
        steps_amount = 0
        total_gen = generic.Gen()
        game = False

async def set_player_name(name):
    global player_name
    player_name = name

async def set_total_word(word):
    global total_word
    total_word = word

async def get_player_name():
    global player_name
    return player_name

async def get_total_word():
    global total_word
    return total_word

async def get_game():
    global game
    return game