# BallGameAnalysisV1.py
from random import random
def printIntro():
    print("start".center(30, '*'))
    print("need ability stat for A B ")


def getInputs():
    a = eval(input('A stat'))
    b = eval(input('B stat'))
    n = eval(input('number of matches'))
    return a, b, n


def printSummary(winsA, winsB):
    n = winsA + winsB
    print('summary'.center(30, '*'))
    print(f'{n}matches in total')
    print(f'A win {winsA} matches, win rate is {winsA/n:0.1%}')
    print(f'B win {winsB} matches, win rate is {winsB/n:0.1%}')


def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simoneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def gameover(scoreA, scoreB):
    return scoreA == 15 or scoreB == 15


def simoneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = 'A'
    while not gameover(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        elif serving == 'B':
            if random() < probB:
                scoreB += 1
            else:
                serving = 'A'
        return scoreA, scoreB


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

main()
