import pygame
import pygame_gui
import profundidad
import amplitud

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
imgFreezer = pygame.image.load("img/freezer.png")
imgFreezer = pygame.transform.scale(imgFreezer, (IMAGE_SIZE, IMAGE_SIZE))
imgCell = pygame.image.load("img/cell.png")
imgCell = pygame.transform.scale(imgCell, (IMAGE_SIZE, IMAGE_SIZE))
imgSemilla = pygame.image.load("img/semilla.png")
imgSemilla = pygame.transform.scale(imgSemilla, (IMAGE_SIZE, IMAGE_SIZE))
imgEsfera = pygame.image.load("img/esfera.png")
imgEsfera = pygame.transform.scale(imgEsfera, (IMAGE_SIZE, IMAGE_SIZE))


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
                    amplitud.bfs(matriz(txt)[0],matriz(txt)[1],matriz(txt)[2])
                elif event.ui_element == button3:
                    print("Costo uniforme")
                elif event.ui_element == button4:
                    print("Profundidad")
                    profundidad.dfs(matriz(txt)[0],matriz(txt)[1],matriz(txt)[2])
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

'''from tkinter import *
from main import GokuSmart

# Creamos la content principal
ventana = Tk()

#titulo de la content
ventana.title('IA')

# Modificamos en tamaño de la content 
ventana.geometry('500x400')

# Crear un marco dentro de la content principal
frame = Frame(ventana)
frame.pack(fill=BOTH, expand=True)

# Agregar el widget de contenido a la content principal
canvas = Canvas(frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Añadir contenido al canvas
content = Frame(canvas)
canvas.create_window((canvas.winfo_reqwidth()/2, 0), window=content, anchor=NW)
print(canvas.winfo_reqwidth()/2)
canvas.config(scrollregion=(0,0,0,4000))

#Activar botones no informada
def no_informada():
     
    for widget in content.winfo_children():
        widget.forget()

    title_label = Label(content, text="BUSQUEDA NO INFORMADA")
    title_label.pack(pady=20)

    boton_amplitud.pack()
    boton_costo_uniforme.pack()
    boton_profundidad.pack()
    boton_atras.pack()
    

#Activar botones de informada  
def informada():
    for widget in content.winfo_children():
        widget.forget()
    title_label = Label(content, text="BUSQUEDA INFORMADA")
    title_label.pack(pady=20)
    boton_avara.pack()
    boton_avara2.pack()
    boton_atras.pack()


def atras():
    for widget in content.winfo_children():
        widget.forget()
    title_label = Label(content, text="PROYECTO UNO - INTELIGENCIA ARTIFICIAL")
    title_label.pack(pady=20)
    boton_no_informada.pack()
    boton_informada.pack()


def algoritmo(str):
    if (str=="amplitud"):
        print("Estoy en amplitud")
    elif (str=="costo_uniforme"):
        print("Estoy en costo uniforme")
    elif (str=="profundidad"):
        print("Estoy en profundidad")
    elif (str=="avara"):
        print("Estoy en avara")
    elif (str=="A*"):
        print("Estoy en A*")
      #  main.GokuSmart()

# Creamos los botones para seleccionar el tipo de busqueda
title_label = Label(content, text="PROYECTO UNO - INTELIGENCIA ARTIFICIAL")
title_label.pack(pady=20)
boton_no_informada = Button(
    content, 
    text='BÚSQUEDA NO INFORMADA',
    command=no_informada,
    cursor='X_cursor'
    )
boton_no_informada.pack()

boton_informada = Button(
    content, 
    text='BÚSQUEDA INFORMADA',
    command=informada,
    cursor='X_cursor'
    )
boton_informada.pack()

#Botones para la seleccion de tipo de busqueda no informada
boton_amplitud = Button(
    content, 
    text='Amplitud',
    command=algoritmo("amplitud"),
    cursor='X_cursor'
    )

boton_costo_uniforme = Button(
    content, 
    text='Costo Uniforme',
    command=algoritmo("costo_uniforme"),
    cursor='X_cursor'
    )

boton_profundidad = Button(
    content, 
    text='Profundidad',
    command=algoritmo("profundidad"),
    cursor='X_cursor'
    )

#Botones para la seleccion de tipo de busqueda informada
boton_avara = Button(
    content, 
    text='Avara',
    command=algoritmo("avara"),
    cursor='X_cursor'
    )

boton_avara2 = Button(
    content, 
    text='A*',
    command=algoritmo("A*"),
    cursor='X_cursor'
    )

#Botón de retroceder

boton_atras =Button(
    content, 
    text='Atrás',
    command=atras,
    cursor='X_cursor'
)
GokuSmart()
content.mainloop()'''
