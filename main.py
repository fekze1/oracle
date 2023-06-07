from source import Word, Sign, DataGraph, WORDID
from database import DATABASE, AMOUNT_OF_SIGNS
from generic import Gen

wordDatabase = []
wordDataGraph = DataGraph()

STREAM = list()

def fill():
    global DATABASE, WORDID, wordDatabase, wordDataGraph
    for i in DATABASE:
        newWord = Word(i, WORDID)
        WORDID += 1

        count = 1
        for j in DATABASE[i]:
            if (j == None):
                count += 1
                continue
            newSign = Sign(j, int(str(newWord.ID) + str(count)), int(str(newWord.ID) + str(count)))
            count += 1

            newWord.addSign(newSign)

        wordDatabase.append(newWord)
        wordDataGraph.addWord(newWord)

def findHyphothesis(gen, wordDB):
    return wordDB[gen.fitness.index(max(gen.fitness))]


def findHyphSign(hypho, currentNode):
    global DATABASE
    prev = str()
    for i in DATABASE[hypho]:
        if (i == currentNode):
            return prev
        prev = i

def findHyphFromSides(gen, sides, wordDB):
    global DATABASE
    maxIndex = 0
    maxFit = 0
    count = 0
    flag = False
    for i in DATABASE:
        for j in DATABASE[i]:
            if (j in sides and j != 'Живое' and j != 'Неживое'):
                flag = True
                break
        count += 1

        if (flag == True):
            if gen.fitness[count] > maxFit:
                maxFit = gen.fitness[count]
                maxIndex = count

        flag = False

    return wordDB[maxIndex - 1]

def game(wordDB, wordDG):
    fill()
    currentNode = str()
    probWord = Word()
    NextNodes = list()
    PrevNodes = list()
    SideNodes = list()
    answer = str()
    gen = Gen()

    print("Живое?")
    answer = input()

    match answer:
        case "yes":
            currentNode = "Живое"
        case "no":
            currentNode = "Неживое"

    gen.addSign(currentNode)
    probWord = findHyphothesis(gen, wordDB)

    while (max(gen.fitness) < 0.8):
        #nextNodes = wordDG.getNextNeighbours(currentNode)

        print(str(findHyphSign(probWord.value, currentNode)) + '?')
        answer = input()

        match answer:
            case "yes":
                currentNode = findHyphSign(probWord.value, currentNode)
                gen.addSign(currentNode)
                probWord = findHyphothesis(gen, wordDB)
            case "no":
                side = wordDG.getSideNeighbours(findHyphSign(probWord.value, currentNode))
                probWord = findHyphFromSides(gen, side, wordDB)
                gen.addSign(findHyphSign(probWord.value, currentNode))
    return probWord.value
