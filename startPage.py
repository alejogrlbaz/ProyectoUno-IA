from tkinter import *
import main

# Creamos la content principal
ventana = Tk()

#titulo de la content
ventana.title('ADA II')

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

content.mainloop()