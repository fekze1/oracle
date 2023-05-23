from source import Word, Sign, DataGraph, WORDID
from database import DATABASE
from questions import questionChoose
from generic import Gen

wordDatabase = []
wordDataGraph = DataGraph()

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

def getQuestion(sign):
    wordID = 1
    for i in DATABASE:
        signID = 1
        for j in DATABASE[i]:
            if (j == sign):
                return int(str(wordID) + str(signID - 1))
            signID += 1
        wordID += 1

wordDataGraph.drawData()

gen = Gen()
currentNode = "START"
probWord = ""
currentQuestionID = 16

print(questionChoose(16))
answer = input()

match answer:
    case "Yes":
        currentNode = "Живое"
        currentQuestionID = 35
    case "No":
        currentNode = "Неживое"
        currentQuestionID = 15

gen.addSign(currentNode)

while (currentNode not in DATABASE):
    currentNodes = []

    print(questionChoose(currentQuestionID))
    answer = input()

    match answer:
        case "Yes":
            currentNodes = wordDataGraph.getNextNeighbours(currentNode)
            currentNode = currentNodes[0]

            gen.addSign(currentNode)
            currentQuestionID = getQuestion(currentNode)

        case "No":
            prevCurr = currentNode
            neighbours = wordDataGraph.getSideNeighbours(currentNode)
            try:
                for i in neighbours:
                    if (i not in gen.signs):
                        currentNode = i
                        break
                if (currentNode == prevCurr):
                    neighbours = wordDataGraph.getPrevNeighbours(currentNode)
                    for i in neighbours:
                        if (i not in gen.signs):
                            currentNode = i
                            break

            except:
                try:
                    neighbours = wordDataGraph.getPrevNeighbours(currentNode)
                    for i in neighbours:
                        if (i not in gen.signs):
                            currentNode = i
                except:
                    break;

            currentQuestionID = getQuestion(currentNode)




