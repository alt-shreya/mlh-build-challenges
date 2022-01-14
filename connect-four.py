from turtle import TurtleScreen
import numpy as np


def createBoard():
    # here we use a numpy array. WHen using Jina, you can replace this with DocArray
    board = np.zeros((6, 7))
    return board


def dropPiece():
    pass


def isValidLocation(board, column):
    pass


def getNextOpenRow():
    pass


gameBoard = createBoard()

gameOver = False
playerTurn = 0

while (gameOver == False):
    # ask player 1 if playerTurn = 0
    if playerTurn == 0:
        column = int(input('Player 1, make your selection from 0 to 6:'))

    # ask player 2

    else:
        column = int(input('Player 2, make your selection from 0 to 6:'))

    playerTurn += 1
    playerTurn = playerTurn % 2

