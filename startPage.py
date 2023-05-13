import pygame
import pygame_gui
import profundidad
import amplitud
import costouniforme
import sys


from open_file import abrir_archivo
pygame.init()


# Configurar ventana de pygame
screen = pygame.display.set_mode((650, 610))
#cono y titulo
pygame.display.set_caption("Goku Smart")
icono=pygame.image.load("img/esfera.png")
pygame.display.set_icon(icono)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (64, 64, 64)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (128, 0, 128)
PINK = (255, 0, 255)
BROWN = (139, 69, 19)

screen.fill(LIGHT_GRAY)

# Crear objeto UIManager
manager = pygame_gui.UIManager((640, 610))

# Cargar imágenes
IMAGE_SIZE = 40
white = pygame.image.load("img/white.png")
white = pygame.transform.scale(white, (IMAGE_SIZE, IMAGE_SIZE))
imgMuro = pygame.image.load("img/muro.png")
imgMuro = pygame.transform.scale(imgMuro, (IMAGE_SIZE, IMAGE_SIZE))
imgGoku = pygame.image.load("img/goku.png")
imgGoku = pygame.transform.scale(imgGoku, (IMAGE_SIZE, IMAGE_SIZE))
imgGoku_Estela = pygame.image.load("img/estela-goku.png")
imgGoku_Estela = pygame.transform.scale(imgGoku_Estela, (IMAGE_SIZE, IMAGE_SIZE))
imgFreezer = pygame.image.load("img/freezer.png")
imgFreezer = pygame.transform.scale(imgFreezer, (IMAGE_SIZE, IMAGE_SIZE))
imgCell = pygame.image.load("img/cell.png")
imgCell = pygame.transform.scale(imgCell, (IMAGE_SIZE, IMAGE_SIZE))
imgSemilla = pygame.image.load("img/semilla.png")
imgSemilla = pygame.transform.scale(imgSemilla, (IMAGE_SIZE, IMAGE_SIZE))
imgEsfera = pygame.image.load("img/esfera.png")
imgEsfera = pygame.transform.scale(imgEsfera, (IMAGE_SIZE, IMAGE_SIZE))


=======
def draw_label(way,file):

    #creamos la martiz incial para comprar las posiciones
     with open(file, "r") as file:
            data = [[int(num) for num in line.split()] for line in file] #archivo de entrada lo pasa a listas

     CELL_SIZE = 40
     MARGIN = 10
     matrix = [[data[i][j] for j in range(10)] for i in range(10)]
     image=imgGoku
     pintados = []
     contador = 0

     for n_pos in way:
      pintados.append(n_pos)
      x=n_pos[0]
      y=n_pos[1]
      objeto_pos_actual = matrix[x][y]

      rect = pygame.Rect((y+1) * (CELL_SIZE + MARGIN) + MARGIN, (x+2) * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE)
      button = pygame_gui.elements.UILabel(rect, "", manager=manager)
      button.set_image(image)

      pygame.time.wait(1000)
      # Actualizar el manager
      time_delta = clock.tick(60) / 1000.0
      manager.update(time_delta)
      manager.draw_ui(screen)
      pygame.display.update()

      uno_pintados = pintados[contador]
      x_ant = uno_pintados[0]
      y_ant = uno_pintados[1]
      
      if objeto_pos_actual == 1:
                    image_ant = imgMuro
      elif objeto_pos_actual == 2:
                    image_ant = white
             
      elif objeto_pos_actual == 3:
                    image_ant = imgFreezer
            
      elif objeto_pos_actual == 4:
                     image_ant = imgCell
             
      elif objeto_pos_actual == 5:
                     image_ant = imgSemilla
             
      elif objeto_pos_actual == 6:
                     image_ant = imgGoku_Estela
             
      else:
                     image_ant = imgGoku_Estela
             

      rect = pygame.Rect((y_ant+1) * (CELL_SIZE + MARGIN) + MARGIN, (x_ant+2) * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE)
      button = pygame_gui.elements.UILabel(rect, "", manager=manager)
      button.set_image(image_ant)

      contador+=1


        # Aquí puedes hacer lo que quieras con el elemento


        
        

#Función para pintar la matriz del archivo que se recibe
def matriz(file):

        with open(file, "r") as file:
            data = [[int(num) for num in line.split()] for line in file] #archivo de entrada lo pasa a listas
        # Configuración de la matriz
        CELL_SIZE = 40
        MARGIN = 10
        matrix = [[data[i][j] for j in range(10)] for i in range(10)]
        start = ()
        goals = []
        # Dibuja la matriz en la pantalla
        buttons=[]

        for i in range(10):
                row=[]
                for j in range(10):
                    if matrix[i][j] == 1:
                        image = imgMuro
                    elif matrix[i][j] == 2:
                        image = imgGoku
                        start = (i,j)
                    elif matrix[i][j] == 3:
                        image = imgFreezer
                    elif matrix[i][j] == 4:
                        image = imgCell
                    elif matrix[i][j] == 5:
                        image = imgSemilla
                    elif matrix[i][j] == 6:
                        image = imgEsfera
                        goals.append((i,j))
                    else:
                        image = white
                    # limit to 1 frames per second.
                    #pygame.time.delay(1000) # Espera por 1 segundo

                    rect = pygame.Rect((j+1) * (CELL_SIZE + MARGIN) + MARGIN, (i+2) * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE)
                    button = pygame_gui.elements.UILabel(rect, "", manager=manager)
                    button.set_image(image)
                    row.append(button)
                buttons.append(row)
                    
                    #text = font.render(str(matrix[i][j]), True, (0, 0, 0))
                   # screen.blit(image, (j * (CELL_SIZE + MARGIN) + MARGIN, i * (CELL_SIZE + MARGIN) + MARGIN))
        # Actualizar la pantalla y manejar eventos de pygame
                 
        return matrix, start, goals
        #screen.blit(image, rect)
'''
def showInterface(self):

         with open(file, "r") as file:
            data = [[int(num) for num in line.split()] for line in file] #archivo de entrada lo pasa a listas
        # Configuración de la matriz
        CELL_SIZE = 40
        MARGIN = 10
        matrix = [[data[i][j] for j in range(10)] for i in range(10)]
        start = ()
        goals = []

        for row in range(10):
            for column in range(10):
                if (matrix[row, column] != 1 and matrix[row, column] != 2 and matrix[row, column] != 5 and matrix[row, column] != 3 and matrix[row, column] != 4 and matrix[row, column] != 6):
                    color = WHITE
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN+LENGTHCELL) * column + MARGIN,
                                      (MARGIN+HIGHCELL) * row + MARGIN,
                                      LENGTHCELL,
                                      HIGHCELL])
                if matrix[row, column] == 1:
                    color = BROWN
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN+LENGTHCELL) * column + MARGIN,
                                      (MARGIN+HIGHCELL) * row + MARGIN,
                                      LENGTHCELL,
                                      HIGHCELL])
                if matrix[row, column] == 2:

                    imagen_redimensionada = pygame.transform.scale(
                        self.__imgMario, (45, 45))
                    screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                        (MARGIN+HIGHCELL) *
                                                        row + MARGIN,
                                                        LENGTHCELL,
                                                        HIGHCELL])
                if matrix[row, column] == 5:

                    imagen_redimensionada = pygame.transform.scale(
                        self.__imgKoopa, (45, 45))
                    screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                        (MARGIN+HIGHCELL) *
                                                        row + MARGIN,
                                                        LENGTHCELL,
                                                        HIGHCELL])
                if matrix[row, column] == 3:

                    imagen_redimensionada = pygame.transform.scale(
                        self.__imgStar, (45, 45))
                    screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                        (MARGIN+HIGHCELL) *
                                                        row + MARGIN,
                                                        LENGTHCELL,
                                                        HIGHCELL])
                if matrix[row, column] == 4:

                    imagen_redimensionada = pygame.transform.scale(
                        self.__imgFlower, (45, 45))
                    screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                        (MARGIN+HIGHCELL) *
                                                        row + MARGIN,
                                                        LENGTHCELL,
                                                        HIGHCELL])
                if matrix[row, column] == 6:

                    imagen_redimensionada = pygame.transform.scale(
                        self.__imgPrincess, (45, 45))
                    screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                        (MARGIN+HIGHCELL) *
                                                        row + MARGIN,
                                                        LENGTHCELL,
                                                        HIGHCELL])
                if matrix[row, column] == 8:
                    imagen_redimensionada = pygame.transform.scale(
                        self.__imgMarioAndPrincess, (45, 45))
                    screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                        (MARGIN+HIGHCELL) *
                                                        row + MARGIN,
                                                        LENGTHCELL,
                                                        HIGHCELL])
        pygame.display.flip()
'''
# Crear botones
button_width = 100
button_height = 40
button_padding = 10
button_start_x = (screen.get_width() - (button_width * 6 + button_padding * 5)) // 2  # Calcular el punto de inicio para la primera fila de botones
button_start_y = 10  # Alineación vertical en la parte superior de la ventana

button1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(
        (button_start_x, button_start_y),
        (button_width, button_height)
    ),
    text="Cargar mundo",
    manager=manager
)

button2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(
        (button_start_x + button_width + button_padding, button_start_y),
        (button_width, button_height)
    ),
    text="Amplitud",
    manager=manager
)

button3 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(
        (button_start_x + (button_width + button_padding) * 2, button_start_y),
        (button_width, button_height)
    ),
    text="Costo uniforme",
    manager=manager
)

button4 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(
        (button_start_x + (button_width + button_padding) * 3, button_start_y),
        (button_width, button_height)
    ),
    text="Profundidad",
    manager=manager
)

button5 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(
        (button_start_x + (button_width + button_padding) * 4, button_start_y),
        (button_width, button_height)
    ),
    text="Avara",
    manager=manager
)

button6 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(
        (button_start_x + (button_width + button_padding) * 5, button_start_y),
        (button_width, button_height)
    ),
    text="Avara*",
    manager=manager
)

# Iniciar bucle de eventos de pygame
m=[]
clock = pygame.time.Clock()
running = True

while running:
    time_delta = clock.tick(60) / 1000.0  # Actualizar el tiempo delta
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Manejar eventos de pygame_gui
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button1:
                    print("Cargar mundo")
                    txt = abrir_archivo()
                    matriz(txt)
                    
                elif event.ui_element == button2:
                    print("Amplitud")
                    draw_label(amplitud.bfs(matriz(txt)[0],matriz(txt)[1],matriz(txt)[2]),txt)
                elif event.ui_element == button3:
                    print("Costo uniforme")
                    #draw_label(costouniforme.ucs(matriz(txt)[0],matriz(txt)[1],matriz(txt)[2]))
                elif event.ui_element == button4:
                    print("Profundidad")
                    draw_label(profundidad.dfs(matriz(txt)[0],matriz(txt)[1],matriz(txt)[2]),txt)
                elif event.ui_element == button5:
                    print("Avara")
                elif event.ui_element == button6:
                    print("Avara*")

        # Actualizar elementos de pygame_gui
        manager.process_events(event)

    # Dibujar elementos en la pantalla
    screen.fill((189,195,199))
    manager.update(time_delta)
    manager.draw_ui(screen)
    
    
    # Actualizar la pantalla de pygame
    pygame.display.flip()

pygame.quit()
