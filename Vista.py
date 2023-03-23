import tkinter as tk
from tkinter import filedialog

class Interfaz:
    def ventana():
        raiz = tk.Tk()

        etiqueta1 = tk.Label(raiz, text='Archivo', font=('Arial Black', 12), bg='orange')
        etiqueta1.grid(row = 0, column=1)
        botonAbrir = tk.Button(raiz, text='Abrir', command=lambda:abrirArchivo(), font=('Arial', 11), bg='lightgreen',  height = 1, width = 20)
        botonAbrir.grid(row=1, column=1)
        botonGuardar = tk.Button(raiz, text='Guardar', font=('Arial', 11), bg='lightgreen',  height = 1, width = 20)
        botonGuardar.grid(row=2, column=1)
        botonGuardarComo = tk.Button(raiz, text='Guardar Como', font=('Arial', 11),  bg='lightgreen',  height = 1, width = 20)
        botonGuardarComo.grid(row=3, column=1)
        botonAnalizar = tk.Button(raiz, text='Analizar', font=('Arial', 11),  bg='lightgreen',  height = 1, width = 20)
        botonAnalizar.grid(row=4, column=1)
        botonErrores = tk.Button(raiz, text='Errores', font=('Arial', 11),  bg='lightgreen',  height = 1, width = 20)
        botonErrores.grid(row=5, column=1)
        botonSalir = tk.Button(raiz, text='Salir', font=('Arial', 11),  bg='lightgreen',  height = 1, width = 20)
        botonSalir.grid(row=6, column=1)


        etiqueta2 = tk.Label(raiz, text='Ayuda', font=('Arial Black', 12), bg='orange')
        etiqueta2.grid(row=0, column=2)
        botonMU = tk.Button(raiz, text='Manual de Usuario', font=('Arial', 11),  bg='lightgreen',  height = 1, width = 20)
        botonMU.grid(row=1, column=2)
        botonMT = tk.Button(raiz, text='Manual Técnico', font=('Arial', 11),  bg='lightgreen',  height = 1, width = 20)
        botonMT.grid(row=2, column=2)
        botonTA = tk.Button(raiz, text='Temas de Ayuda', font=('Arial', 11),  bg='lightgreen',  height = 1, width = 20)
        botonTA.grid(row=3, column=2)


        def abrirArchivo():
            newWindow = tk.Toplevel(raiz)
            cuadroTexto = tk.Text(newWindow) 
            cuadroTexto.grid(row=0, column=0)
            newWindow.geometry('600x600')
            archivo = filedialog.askopenfile(mode='r+')
            if not archivo:
                return
            with open(archivo.name, "r+") as archivoAbierto:
                cuadroTexto.delete(1.0, tk.END)
                texto = archivoAbierto.read()
                cuadroTexto.insert(1.0, texto)

        def guardarArchivo(archivo):
            pass

            




        raiz.title('Proyecto 1')
        raiz.configure(bg='orange') 
        raiz.geometry('380x210')
        raiz.mainloop()



