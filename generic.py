from database import AMOUNT_OF_WORDS, AMOUNT_OF_SIGNS, DATABASE
from collections import deque

class Gen:
    def __init__(self):
        self.signs = deque(maxlen=AMOUNT_OF_SIGNS)
        self.fitness = [0 for i in range(AMOUNT_OF_WORDS)]

    def addSign(self, sign):
        self.signs.append(sign)
        self.calcFitness()
    def calcFitness(self):
        word_ind = 0
        for word in DATABASE:
            amount = 0
            for sign in DATABASE[word]:
                if (sign in list(self.signs) and sign != None):
                    amount += 1
            self.fitness[word_ind] = amount / (AMOUNT_OF_SIGNS - DATABASE[word].count(None))
            word_ind += 1
        return self.fitness

    def getProbWordrID(self):
        return self.fitness.index(max(self.fitness))