from main import *
import itertools
import pygame 
import random

class Game_board:

    # Loading big images
    sheep = pygame.image.load('Sheep2.png') 
    wolf = pygame.image.load('Wolf2.png')

    board = [[0]*8 for _ in range(8)]

    Blue = pygame.Color(0, 255, 255)
    Yellow = pygame.Color(253, 223, 72)
    
    res = (720, 720)

    screen = pygame.display.set_mode(res)
    clock = pygame.time.Clock()

    colors = itertools.cycle((Blue, Yellow))

    ts = 64

    width, height = 8*ts, 8*ts
    
    background = pygame.Surface((width, height))

    #Criação do quadro
    for y in range(0, height, ts):
        for x in range(0, width, ts):
            rect = (x, y, ts, ts)
            if y == 7 and x == 4:
                screen.blit(self.sheep, rect)
            else:
                pygame.draw.rect(background, next(colors), rect)
        next(colors)



    running = True
    while running:
        events = pygame.event.get()
        
        for event in events:
            #Quando é carregada a tecla ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
            #Quando é carregado a cruz da janela para sair do programa
            elif event.type == pygame.QUIT:
                running = False    

        screen.blit(background, (100, 100))
        
        pygame.display.flip()

    pygame.quit()