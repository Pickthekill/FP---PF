from main import *
import itertools
import pygame 

class Game_board:

    # Loading big images
    sheep = pygame.image.load('Sheep2.png') 
    wolf = pygame.image.load('Wolf2.png')

    board = [[0]*8 for _ in range(8)]

    Blue = pygame.Color(0, 255, 255)
    Yellow = pygame.Color(253, 223, 72)
    LYellow = pygame.Color(255, 229, 158)
    
    res = (720, 720)

    screen = pygame.display.set_mode(res)
    clock = pygame.time.Clock()

    colors = itertools.cycle((Blue, Yellow))

    pos_wolf1 = [164, 100]
    pos_wolf2 = [292, 100]
    pos_wolf3 = [420, 100]
    pos_wolf4 = [548, 100]
    pos_sheep = [360, 548]

    squarepos_wolf1 = [164, 100, 64, 64]
    squarepos_wolf2 = [292, 100, 64, 64]
    squarepos_wolf3 = [420, 100, 64, 64]
    squarepos_wolf4 = [548, 100, 64, 64]
    squarepos_sheep = [356, 548, 64, 64] 
    
    ts = 64

    rect_size = (64, 64)

    width, height = 8*ts, 8*ts
    
    background = pygame.Surface((width, height))

    turn = 1


    #Criação do quadro
    for y in range(0, height, ts):
        for x in range(0, width, ts):
            rect = (x, y, ts, ts)
            pygame.draw.rect(background, next(colors), rect)
        next(colors)

    # Se for 1 é o turno da ovelha, se for 0 é o turno dos Lobos
    player_turn = 1

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
        
            mouse = pygame.mouse.get_pos()  

            screen.blit(background, (100,100))

            if player_turn == 1:
                pygame.draw.rect(screen, LYellow, squarepos_sheep)
                if pos_sheep[0] <= mouse[0] <= pos_sheep[0]+64 and pos_sheep[1] <= mouse[1] <= pos_sheep[1]+64:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        opc_sheep1 = squarepos_sheep
                        opc_sheep2 = squarepos_sheep
                        opc_sheep3 = squarepos_sheep
                        opc_sheep4 = squarepos_sheep

                        #Quadrado cima da esquerda
                        if squarepos_sheep[0] > 0:
                            opc_sheep1[0] -= squarepos_sheep - 64
                            opc_sheep1[1] -= squarepos_sheep - 64
                            pygame.draw.rect(screen, LYellow, opc_sheep1)
                            if opc_wolf1[0] <= mouse[0] <= opc_wolf1[0]+64 and opc_wolf1[1] <= mouse[1] <= opc_wolf1[1]+64:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos_sheep[0] = opc_sheep1[0]
                                    pos_sheep[1] = opc_sheep1[1]
                        
                        #Quadrado cima da direita
                        if squarepos_sheep[0] < 448:
                            opc_sheep2[0] += squarepos_sheep + 64
                            opc_sheep2[1] -= squarepos_sheep - 64
                            pygame.draw.rect(screen, LYellow, opc_sheep2)
                            if opc_wolf1[0] <= mouse[0] <= opc_wolf1[0]+64 and opc_wolf1[1] <= mouse[1] <= opc_wolf1[1]+64:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos_sheep[0] = opc_sheep2[0]
                                    pos_sheep[1] = opc_sheep2[1]
                        
                        #Quadrado baixo da esquerda
                        if squarepos_sheep[1] > 0:
                            opc_sheep3[0] -= squarepos_sheep - 64
                            opc_sheep3[1] += squarepos_sheep + 64
                            pygame.draw.rect(screen, LYellow, opc_sheep3)
                            if opc_wolf1[0] <= mouse[0] <= opc_wolf1[0]+64 and opc_wolf1[1] <= mouse[1] <= opc_wolf1[1]+64:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos_sheep[0] = opc_sheep3[0]
                                    pos_sheep[1] = opc_sheep3[1]
                        
                        #Quadrado baixo da direita
                        if squarepos_sheep[1] < 448:
                            opc_sheep4[0] += squarepos_sheep + 64
                            opc_sheep4[1] += squarepos_sheep + 64
                            pygame.draw.rect(screen, LYellow, opc_sheep4)
                            if opc_wolf1[0] <= mouse[0] <= opc_wolf1[0]+64 and opc_wolf1[1] <= mouse[1] <= opc_wolf1[1]+64:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos_sheep[0] = opc_sheep4[0]
                                    pos_sheep[1] = opc_sheep4[1]
                            
                player_turn = 0
        
            if player_turn == 0:
                screen.blit(background, (100,100))
                pygame.draw.rect(screen, LYellow, squarepos_wolf1)
                pygame.draw.rect(screen, LYellow, squarepos_wolf2)
                pygame.draw.rect(screen, LYellow, squarepos_wolf3)
                pygame.draw.rect(screen, LYellow, squarepos_wolf4)

                #Opções do Lobo 1
                if squarepos_wolf1[0] <= mouse[0] <= squarepos_wolf1[0]+64 and squarepos_wolf1[1] <= mouse[1] <= squarepos_wolf1[1]+64:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        opc_wolf1 = squarepos_wolf1
                        opc_wolf2 = squarepos_wolf1

                        if squarepos_wolf1[0] > 100 and squarepos_wolf1[1] < 550:
                            opc_wolf1[0] = squarepos_wolf1[0] - 64
                            opc_wolf1[1] = squarepos_wolf1[1] + 64
                            screen.blit(background, (100,100))
                            pygame.draw.rect(screen, LYellow, opc_wolf1)
                            if opc_wolf1[0] <= mouse[0] <= opc_wolf1[0]+64 and opc_wolf1[1] <= mouse[1] <= opc_wolf1[1]+64:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos_wolf1[0] = opc_wolf1[0]
                                    pos_wolf1[1] = opc_wolf1[1]

                        if squarepos_wolf1[0] > 100 and squarepos_wolf1[1] < 550:
                            opc_wolf2[0] = squarepos_wolf1[0] + 64
                            opc_wolf2[1] = squarepos_wolf1[1] + 64
                            screen.blit(background, (100,100))
                            pygame.draw.rect(screen, LYellow, opc_wolf2)

                            if opc_wolf2[0] <= mouse[0] <= opc_wolf2[0]+64 and opc_wolf2[1] <= mouse[1] <= opc_wolf2[1]+64:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        pos_wolf1[0] = opc_wolf2[0]
                                        pos_wolf1[1] = opc_wolf2[1]
                #Opções do Lobo 2
                if squarepos_wolf2[0] <= mouse[0] <= squarepos_wolf2[0]+64 and squarepos_wolf2[1] <= mouse[1] <= squarepos_wolf2[1]+64:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        opc_wolf1 = squarepos_wolf2
                        opc_wolf2 = squarepos_wolf2

                        if squarepos_wolf1[0] > 100 and squarepos_wolf1[1] < 550:
                            opc_wolf1[0] = squarepos_wolf2[0] - 64
                            opc_wolf1[1] = squarepos_wolf2[1] + 64
                            screen.blit(background, (100,100))
                            pygame.draw.rect(screen, LYellow, opc_wolf1)

                            if opc_wolf1[0] <= mouse[0] <= opc_wolf1[0]+64 and opc_wolf1[1] <= mouse[1] <= opc_wolf1[1]+64:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos_wolf2[0] = opc_wolf1[0]
                                    pos_wolf2[1] = opc_wolf1[1]

                        if squarepos_wolf1[0] > 100 and squarepos_wolf1[1] < 550:
                            opc_wolf2[0] = squarepos_wolf2[0] + 64
                            opc_wolf2[1] = squarepos_wolf2[1] + 64
                            screen.blit(background, (100,100))
                            pygame.draw.rect(screen, LYellow, opc_wolf2)

                            if opc_wolf2[0] <= mouse[0] <= opc_wolf2[0]+64 and opc_wolf2[1] <= mouse[1] <= opc_wolf2[1]+64:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        pos_wolf2[0] = opc_wolf2[0]
                                        pos_wolf2[1] = opc_wolf2[1]

                #Opções do Lobo 3
                if squarepos_wolf3[0] <= mouse[0] <= squarepos_wolf3[0]+64 and squarepos_wolf3[1] <= mouse[1] <= squarepos_wolf3[1]+64:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        opc_wolf1 = squarepos_wolf3
                        opc_wolf2 = squarepos_wolf3

                        if squarepos_wolf1[0] > 100 and squarepos_wolf1[1] < 550:
                            opc_wolf1[0] = squarepos_wolf3[0] - 64
                            opc_wolf1[1] = squarepos_wolf3[1] + 64
                            screen.blit(background, (100,100))
                            pygame.draw.rect(screen, LYellow, opc_wolf1)
                            if opc_wolf1[0] <= mouse[0] <= opc_wolf1[0]+64 and opc_wolf1[1] <= mouse[1] <= opc_wolf1[1]+64:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos_wolf3[0] = opc_wolf1[0]
                                    pos_wolf3[1] = opc_wolf1[1]

                        if squarepos_wolf1[0] > 100 and squarepos_wolf1[1] < 550:
                            opc_wolf2[0] = squarepos_wolf3[0] + 64
                            opc_wolf2[1] = squarepos_wolf3[1] + 64
                            screen.blit(background, (100,100))
                            pygame.draw.rect(screen, LYellow, opc_wolf2)
                            if opc_wolf2[0] <= mouse[0] <= opc_wolf2[0]+64 and opc_wolf2[1] <= mouse[1] <= opc_wolf2[1]+64:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        pos_wolf3[0] = opc_wolf2[0]
                                        pos_wolf3[1] = opc_wolf2[1]

                #Opções do Lobo 4
                if squarepos_wolf4[0] <= mouse[0] <= squarepos_wolf4[0]+64 and squarepos_wolf4[1] <= mouse[1] <= squarepos_wolf4[1]+64:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        opc_wolf1 = squarepos_wolf4
                        opc_wolf2 = squarepos_wolf4

                        if squarepos_wolf1[0] > 100 and squarepos_wolf1[1] < 550:
                            opc_wolf1[0] = squarepos_wolf4[0] - 64
                            opc_wolf1[1] = squarepos_wolf4[1] + 64
                            screen.blit(background, (100,100))
                            pygame.draw.rect(screen, LYellow, opc_wolf1)
                            if opc_wolf1[0] <= mouse[0] <= opc_wolf1[0]+64 and opc_wolf1[1] <= mouse[1] <= opc_wolf1[1]+64:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos_wolf4[0] = opc_wolf1[0]
                                    pos_wolf4[1] = opc_wolf1[1]

                        if squarepos_wolf1[0] > 100 and squarepos_wolf1[1] < 550:
                            opc_wolf2[0] = squarepos_wolf4[0] + 64
                            opc_wolf2[1] = squarepos_wolf4[1] + 64
                            screen.blit(background, (100,100))
                            pygame.draw.rect(screen, LYellow, opc_wolf2)

                            if opc_wolf2[0] <= mouse[0] <= opc_wolf2[0]+64 and opc_wolf2[1] <= mouse[1] <= opc_wolf2[1]+64:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        pos_wolf4[0] = opc_wolf2[0]
                                        pos_wolf4[1] = opc_wolf2[1]
            else:
                pass
        
            screen.blit(sheep, pos_sheep)
            screen.blit(wolf, pos_wolf1)
            screen.blit(wolf, pos_wolf2)
            screen.blit(wolf, pos_wolf3)
            screen.blit(wolf, pos_wolf4)


        pygame.display.flip()

    pygame.quit()