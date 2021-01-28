import pygame
import time
from game import *

def main():
    pygame.init()

    #Resolução do ecrã e incializar o menu
    resX = 1280
    resY = 720
    res = (resX, resY)

    screen = pygame.display.set_mode(res)
    
    exitbutton = (resX/2+80, resY/2+140)
    playbutton = (resX/2+80, resY/2+80)
    
    # cor do fundo  
    backcolor = (0, 0, 0)

    # cor do titulo
    title_color = (128, 223, 255)
    
    # cor mais clara
    color_light = (255, 255, 255) 
    
    # cor mais escura  
    color_dark = (255, 230, 128)
    
    # Font do texto
    txtfont = pygame.font.Font('Roboto-Regular.ttf', 35)  
    
    # Font do titulo
    titlefont = pygame.font.Font('StardosStencil-Bold.ttf', 100)

    # Renderizar o texto escrito
    Title_text = titlefont.render('WOLF & SHEEP' , True , title_color)
    Quit_text = txtfont.render('Quit' , True , backcolor)
    Start_text = txtfont.render('Start' , True , backcolor)

    # Carregar as imagens
    image = pygame.image.load('Sheep.png') 
    image2 = pygame.image.load('Wolf.png') 


    while True:  
        events = pygame.event.get()
        
        for event in events:

            #Quando é carregada a tecla ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                    
            #Quando é carregado a cruz da janela para sair do programa
            elif event.type == pygame.QUIT:
                exit()            
                    
            #Preenche o ecrã
            screen.fill(backcolor)  

            #Posição do rato
            mouse = pygame.mouse.get_pos()  
            
            #Ao colocar o rato por cima do botão Quit
            if resX/2-60 <= mouse[0] <= exitbutton[0] and resY/2+100 <= mouse[1] <= exitbutton[1]:  
                pygame.draw.rect(screen,color_light,[resX/2-60,resY/2+100,140,40])  
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                   exit()
            else:  
                pygame.draw.rect(screen,color_dark,[resX/2-60,resY/2+100,140,40])  

            #Ao colocar o rato por cima do botão Start
            if resX/2-60 <= mouse[0] <= playbutton[0] and resY/2+40 <= mouse[1] <= playbutton[1]:  
                pygame.draw.rect(screen,color_light,[resX/2-60,resY/2+40,140,40])  
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                   game.game()
                   main = False
            else:  
                pygame.draw.rect(screen,color_dark,[resX/2-60,resY/2+40,140,40])  
            
            # Colocar o texto na caixa  
            screen.blit(Quit_text, (resX/2-25,resY/2+100))  
            screen.blit(Start_text, (resX/2-27,resY/2+40))  
            screen.blit(Title_text, (resX/2-380,resY/2-260))
            screen.blit(image, (resX-356, resY/2-20))
            screen.blit(image2, (100, resY/2-20)) 


            # Atualizar os frames do jogo
            pygame.display.update()

main()