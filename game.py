import pygame
from board import *

pygame.init()

def updateTiles(board, square, i, newBoard):
    neighbors = 0
    if board[i - 1][3]:
        neighbors += 1
    if board[i - 14][3]:
        neighbors += 1
    if board[i - 15][3]:
        neighbors += 1
    if board[i - 13][3]:
        neighbors += 1
    if len(board) - i > 1:
        if board[i + 1][3]:
            neighbors += 1
    if len(board) - i > 13:
        if board[i + 13][3]:
            neighbors += 1
    if len(board) - i > 14:
        if board[i + 14][3]:
            neighbors += 1
    if len(board) - i > 15:
        if board[i + 15][3]:
            neighbors += 1

    if neighbors == 3 and board[i][3] == False:
        newBoard[i] = update(newBoard[i], 1)
    elif neighbors <= 1 or neighbors >= 4:
        newBoard[i] = update(newBoard[i], 2)
    return newBoard