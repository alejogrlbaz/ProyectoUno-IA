from tkinter import filedialog

def abrir_archivo():

    global ruta_archivo
    # Definimos los tipos de archivo permitidos
    tipos_archivo = [('Archivos de texto', '*.txt')]
    # Abrimos el diálogo para seleccionar el archivo
    ruta_archivo = filedialog.askopenfilename(defaultextension='.txt', filetypes=tipos_archivo )
    
    # Verificamos si se seleccionó un archivo
    if ruta_archivo != '':

        return ruta_archivo