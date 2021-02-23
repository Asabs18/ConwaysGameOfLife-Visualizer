import pygame
from assets import *
from button import *

pygame.init()

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

startBtn = MyButton(screen, "Start", 220, SCREENHEIGHT - 103, 400, 150, BTNCOLOR)
stopBtn = MyButton(screen, "Stop", 220, SCREENHEIGHT - 103, 400, 150, BTNCOLOR)
clearBtn = MyButton(screen, "Clear", 576, SCREENHEIGHT - 142, 300, 72, BTNCOLOR)
resetBtn = MyButton(screen, "Reset", 576, SCREENHEIGHT - 64, 300, 72, BTNCOLOR)

def createBoard():
    board = []
    dentx = 1
    denty = 1
    for x in range(SCREENWIDTH):
        for y in range(SCREENHEIGHT - 766):
            board.append((pygame.Rect(x*BLOCKSIZE + dentx, y*BLOCKSIZE + denty, BLOCKSIZE, BLOCKSIZE), x*BLOCKSIZE + dentx, y*BLOCKSIZE + denty, False))
            denty += 1
        dentx += 1
        denty = 1
    return board

def update(square, val=0):
    change = True
    if val == 2:
        change = False
    if val == 0:
        if square[3] == True:
            change = False
    return (square[0], square[1], square[2], change)

def changeSquare(pos, board):
    for i, square in enumerate(board):
        if square[0].collidepoint(pos):
            board[i] = update(square)
            break
    
    return board

def drawBoard(screen, board, play):
    for i, square in enumerate(board):
        if square[3] == False:
            pygame.draw.rect(screen, BGCOLOR, square[0])
        else:
            pygame.draw.rect(screen, FILLCOLOR, square[0])
    if play:
        stopBtn.draw_button()
    else:
        startBtn.draw_button()
    clearBtn.draw_button()
    resetBtn.draw_button()
