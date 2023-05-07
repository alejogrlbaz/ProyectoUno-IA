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
    boton_amplitud.pack()
    boton_costo_uniforme.pack()
    boton_profundidad.pack()

    boton_informada.forget()

#Activar botones de informada  
def informada():
    boton_avara.pack()
    boton_costo_uniforme.pack()
    boton_profundidad.pack()

def algoritmo(str):
    if(str=="Amplitud"):
        print("Estoy en amplitud")
        main.GokuSmart()

# Creamos los botones para seleccionar el tipo de busqueda
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
    command=algoritmo("Amplitud"),
    cursor='X_cursor'
    )

boton_costo_uniforme = Button(
    content, 
    text='Costo Uniforme',
    #command=limpiar_pantalla,
    cursor='X_cursor'
    )

boton_profundidad = Button(
    content, 
    text='Profundidad',
    #command=limpiar_pantalla,
    cursor='X_cursor'
    )

#Botones para la seleccion de tipo de busqueda informada
boton_avara = Button(
    content, 
    text='Avara',
    #command=limpiar_pantalla,
    cursor='X_cursor'
    )

boton_avara2 = Button(
    content, 
    text='A*',
    #command=limpiar_pantalla,
    cursor='X_cursor'
    )

content.mainloop()