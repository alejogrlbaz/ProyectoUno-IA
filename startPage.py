import pygame
import pygame_gui
import profundidad

from open_file import abrir_archivo
pygame.init()

# Configurar ventana de pygame
screen = pygame.display.set_mode((640, 610))
pygame.display.set_caption("Goku Smart")

# Crear objeto UIManager
manager = pygame_gui.UIManager((640, 610))

# Cargar imágenes
IMAGE_SIZE = 40
white = pygame.image.load("img/white.png")
white = pygame.transform.scale(white, (IMAGE_SIZE, IMAGE_SIZE))
imgMuro = pygame.image.load("img/muro.png")
imgMuro = pygame.transform.scale(imgMuro, (IMAGE_SIZE, IMAGE_SIZE))
imgGoku = pygame.image.load("img/goku.jpg")
imgGoku = pygame.transform.scale(imgGoku, (IMAGE_SIZE, IMAGE_SIZE))
imgFreezer = pygame.image.load("img/freezer.png")
imgFreezer = pygame.transform.scale(imgFreezer, (IMAGE_SIZE, IMAGE_SIZE))
imgCell = pygame.image.load("img/cell.png")
imgCell = pygame.transform.scale(imgCell, (IMAGE_SIZE, IMAGE_SIZE))
imgSemilla = pygame.image.load("img/semilla.png")
imgSemilla = pygame.transform.scale(imgSemilla, (IMAGE_SIZE, IMAGE_SIZE))
imgEsfera = pygame.image.load("img/esfera.png")
imgEsfera = pygame.transform.scale(imgEsfera, (IMAGE_SIZE, IMAGE_SIZE))


def draw_label(way):
    CELL_SIZE = 40
    MARGIN = 10
    image=imgGoku
    for x in way:
        i=x[0]
        j=x[1]
        rect = pygame.Rect((j+1) * (CELL_SIZE + MARGIN) + MARGIN, (i+2) * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE)
        button = pygame_gui.elements.UILabel(rect, "", manager=manager)
        button.set_image(image)


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

                    rect = pygame.Rect((j+1) * (CELL_SIZE + MARGIN) + MARGIN, (i+2) * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE)
                    button = pygame_gui.elements.UILabel(rect, "", manager=manager)
                    button.set_image(image)
                    row.append(button)
                buttons.append(row)
                    
                    #font = pygame.font.SysFont(None, 30)
                    
                    #text = font.render(str(matrix[i][j]), True, (0, 0, 0))
                   # screen.blit(image, (j * (CELL_SIZE + MARGIN) + MARGIN, i * (CELL_SIZE + MARGIN) + MARGIN))
        return matrix, start, goals
        #screen.blit(image, rect)


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
                elif event.ui_element == button3:
                    print("Costo uniforme")
                elif event.ui_element == button4:
                    print("Profundidad")
                    draw_label(profundidad.dfs(matriz(txt)[0],matriz(txt)[1],matriz(txt)[2]))
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
