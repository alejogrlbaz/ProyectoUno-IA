#from typing import Self
import pygame
from tkinter import *
from open_file import abrir_archivo


class GokuSmart:

    def __init__(self):
        #ppal = Tk()
        #ppal.title("Goku Smart")
        #ppal.geometry("500x500")
        # Pygame
        pygame.init()

        # tamaño de pygame
        SCREEN_WIDTH = 610
        SCREEN_HEIGHT = 610
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("GOKU SMART")

        # Cargar imágenes
        IMAGE_SIZE = 50
        white = pygame.image.load("img/white.png")
        white = pygame.transform.scale(white, (IMAGE_SIZE, IMAGE_SIZE))
        imgMuro = pygame.image.load("img/muro.png")
        imgMuro = pygame.transform.scale(imgMuro, (IMAGE_SIZE, IMAGE_SIZE))
        imgGoku = pygame.image.load("img/goku.png")
        imgGoku = pygame.transform.scale(imgGoku, (IMAGE_SIZE, IMAGE_SIZE))
        imgFreezer = pygame.image.load("img/freezer.png")
        imgFreezer = pygame.transform.scale(imgFreezer, (IMAGE_SIZE, IMAGE_SIZE))
        imgCell = pygame.image.load("img/cell.png")
        imgCell = pygame.transform.scale(imgCell, (IMAGE_SIZE, IMAGE_SIZE))
        imgSemilla = pygame.image.load("img/semilla.png")
        imgSemilla = pygame.transform.scale(imgSemilla, (IMAGE_SIZE, IMAGE_SIZE))
        imgEsfera = pygame.image.load("img/esfera.png")
        imgEsfera = pygame.transform.scale(imgEsfera, (IMAGE_SIZE, IMAGE_SIZE))

        #carga de archivo
        file = ""
        
        #print(self.data)

        with open(file, "r") as file:
            data = [[int(num) for num in line.split()] for line in file] #archivo de entrada lo pasa a listas
            print(data[0][0])
            print(data[0][1])
        # Configuración de la matriz
        CELL_SIZE = 50
        MARGIN = 10
        matrix = [[data[i][j] for j in range(10)] for i in range(10)]
        print(matrix)
        # Dibuja la matriz en la pantalla
        
        for i in range(10):
                for j in range(10):
                    if matrix[i][j] == 1:
                        image = imgMuro
                    elif matrix[i][j] == 2:
                        image = imgGoku
                    elif matrix[i][j] == 3:
                        image = imgFreezer
                    elif matrix[i][j] == 4:
                        image = imgCell
                    elif matrix[i][j] == 5:
                        image = imgSemilla
                    elif matrix[i][j] == 6:
                        image = imgEsfera

                    else:
                        image = white
                    rect = pygame.Rect(j * (CELL_SIZE + MARGIN) + MARGIN, i * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE)
                    #font = pygame.font.SysFont(None, 30)
                    
                    #text = font.render(str(matrix[i][j]), True, (0, 0, 0))
                   # screen.blit(image, (j * (CELL_SIZE + MARGIN) + MARGIN, i * (CELL_SIZE + MARGIN) + MARGIN))

                    screen.blit(image, rect)

        # Bucle principal del juego
        running = True
        while running:
            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Actualizar la pantalla
            screen.fill((0, 0, 0))
            draw_matrix()
            pygame.display.flip()

        # Salir de Pygame
        pygame.quit()
        #ppal.mainloop()

    
 #GokuSmart()