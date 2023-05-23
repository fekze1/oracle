import matplotlib.pyplot as plt
import networkx as nx

WORDID = 1

def findWordID():
    global WORDID
    WORDID += 1
    return WORDID - 1

class Sign:
    def __init__(self, newValue=None, newID=None, newQuestionID=None):
        self.value = newValue
        self.ID = newID
        self.questionID = newQuestionID


class Word:
    def __init__(self, newValue=None, newID=None):
        global WORDID
        self.value = newValue
        self.ID = newID
        self.signsQueue = []

    def addSign(self, newSign):
        self.signsQueue.append(newSign)

class DataGraph:
    def __init__(self):
        self.data = nx.MultiDiGraph()
        self.data.add_node("START")

    def addWord(self, word):
        self.data.add_node(word.value)

        prev = word.value
        for sign in word.signsQueue:
            self.data.add_node(sign.value)
            self.data.add_edge(sign.value, prev)
            prev = sign.value
        self.data.add_edge("START", prev)

    def getNextNeighbours(self, signValue):
        return list(self.data.neighbors(signValue))

    def getPrevNeighbours(self, signValue):
        reversed = self.data.reverse()
        return list(reversed.neighbors(signValue))

    def getSideNeighbours(self, signValue):
        prev = list(self.getPrevNeighbours(signValue))[0]
        neighbours = self.getNextNeighbours(prev)
        if (neighbours[0] == signValue):
            return None

        neighbours.remove(signValue)

        return neighbours

    def drawData(self):

        nx.draw_shell(self.data, with_labels=True)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        # plt.tight_layout()
        plt.show()
