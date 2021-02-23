import pygame, sys, copy
from assets import *
from board import *
from game import *

FONT = pygame.font.SysFont("comicsans", 25)
gen = 0

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("Conway's Game of Life")
board = createBoard()
newBoard = createBoard()
startBoard = createBoard()

i = 0
run = True
play = False
while run:
    i += 1
    clock.tick(100)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and play == False:
            board = changeSquare(pos, board)
        if pygame.mouse.get_pressed() == (1,0,0):
            if clearBtn.rect.collidepoint(pygame.mouse.get_pos()):
                board = createBoard()
                newBoard = createBoard()
                startBoard = createBoard()
            if play == False:
                if startBtn.rect.collidepoint(pygame.mouse.get_pos()):
                    play = True
                    newBoard = copy.deepcopy(board)
                    startBoard = copy.deepcopy(board)
            else:
                if stopBtn.rect.collidepoint(pygame.mouse.get_pos()):
                    play = False
            if resetBtn.rect.collidepoint(pygame.mouse.get_pos()):
                board = copy.deepcopy(startBoard)
                gen = 0

    if play and i >= 50:
        gen += 1
        for i, square in enumerate(newBoard):
            newBoard = updateTiles(board, square, i, newBoard)
        board = copy.deepcopy(newBoard)
        i = 0
    screen.fill(WALLCOLOR)
    drawBoard(screen, board, play)
    text = FONT.render("Gen: " + str(gen), 1, (255, 255, 255))
    screen.blit(text, (SCREENWIDTH - text.get_width() - 10, SCREENHEIGHT - 20))
    pygame.display.flip()

pygame.quit()