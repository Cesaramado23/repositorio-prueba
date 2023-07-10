import tkinter as tk
from tkinter import ttk
from tkinter import *
from functools import partial

def abrir_ventana_secundaria():
    # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.config(width=300, height=200)
    # Crear un botón dentro de la ventana secundaria
    # para cerrar la misma.
    boton_cerrar = ttk.Button(
        ventana_secundaria,
        text="Cerrar ventana", 
        command=ventana_secundaria.destroy
    )
    boton_cerrar.place(x=75, y=75)

def Ingresar_Datos(ancho=430, alto=330, lista = [], botones=[]):
    # Crear una ventana secundaria.
    Ingresar = tk.Toplevel()
    Ingresar.title("Ingresar Datos")
    Ingresar.config(width=ancho, height=alto)
    Ingresar.config(bg="orange")
    # Crear un botón dentro de la ventana secundaria
    # para cerrar la misma.
    pos=0.02
    siguiente = 0.12
    for data in lista:
        Label(Ingresar, text=data['label']).place(relx=0.02, rely=pos,relwidth=0.4, relheight=0.1)
        entry = Entry(Ingresar)
        entry.place(relx=0.45, rely=pos,relwidth=0.52, relheight=0.1)
        data['input'] =entry 
        pos+=siguiente
    
    for boton in botones:
        boton = ttk.Button(Ingresar, **boton)
        boton.place(relx=0.02, rely=pos,relwidth=0.95, relheight=0.1)
        pos+=siguiente
    
    boton_cerrar = ttk.Button(
        Ingresar,
        text="Salir", 
        command=Ingresar.destroy
    )
    boton_cerrar.place(relx=0.02, rely=pos, relwidth=0.95, relheight=0.1)
    # boton_cerrar.config(bg="#000000")
    # boton_cerrar.config(fg="red")
    centrar(Ingresar)
    return Ingresar ,lista

def Mostrar_Datos(ancho=430, alto=330, lista = [], datos = []):
    # Crear una ventana secundaria.
    ventana = tk.Toplevel()
    ventana.title('Datos')
    ventana.geometry('600x500')
    # ventana['bg']='#fb0'
    campos = []
    for data in lista:
        campos.append(data['label'])
        
    tabla = ttk.Treeview(ventana, columns=campos)
    tabla.column("#0",width=40)
    tabla.heading("#0", text="Item", anchor=CENTER)
    for data in campos:
        tabla.column(data,width=100, anchor=CENTER)
        tabla.heading(data, text=data, anchor=CENTER)
    
    for i, data in enumerate(datos):
        valor = []
        for val in campos:
            valor.append(data[val])
        tabla.insert("",END, text=str(i+1), values=valor)
    
    tabla.place(relx=0.02, rely=0.02,relwidth=0.96, relheight=0.7)
    boton_cerrar = ttk.Button(
        ventana,
        text="Salir", 
        command=ventana.destroy
    )
    boton_cerrar.place(relx=0.02, rely=0.75, relwidth=0.95, relheight=0.1)
    # centrar(ventana)


    # ventana.mainloop()

def Menu(ancho=450, alto=350, titulo_pantalla="Ventana principal", titulo='MENU', opciones=[]):
    # Crear la ventana principal.
    ventana_principal = tk.Tk()
    
    ventana_principal.title(titulo_pantalla)
    
    frame=Frame(ventana_principal)
    frame.pack()      
    frame.config(bg="purple") 
    Label(frame, text=titulo).place(relx=0.02, rely=0.02,relwidth=0.95, relheight=0.1)
    
    pos=0.14
    siguiente = 0.12
    for opcion in opciones:

        boton_abrir = ttk.Button(
            frame,
            **opcion
        )
        boton_abrir.place(relx=0.02, rely=pos, relwidth=0.95, relheight=0.1)
        pos+=siguiente
    
    
    boton_abrir1 = ttk.Button(
        frame,
        text="Salir",
        command=ventana_principal.destroy
    )
    
    boton_abrir1.place(relx=0.02, rely=pos, relwidth=0.95, relheight=0.1)
    ventana_principal.config(width=ancho, height=alto)
    frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    centrar(ventana_principal)
    ventana_principal.mainloop()
    return ventana_principal

def centrar(r):
    altura = r.winfo_reqheight()
    anchura = r.winfo_reqwidth()
    altura_pantalla = r.winfo_screenheight()
    anchura_pantalla = r.winfo_screenwidth()
    # print(f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")
    x = (anchura_pantalla // 2) - (anchura//2)
    y = (altura_pantalla//2) - (altura//2)
    r.geometry(f"+{x}+{y}")


def Funcion1():
    print('Funcion 1')
def Funcion2():
    print('Funcion 2')
def Funcion3():
    print('Funcion 3')
    
if __name__ == "__main__":
    botones = [{'text': 'Boton 1', 'command':Funcion1},
            {'text': 'Boton 2', 'command':Funcion2},
            {'text': 'Boton 3', 'command':Funcion3}
    ]
    formulario=[
        {'label':'uno'},
        {'label':'dos'},
        {'label':'tres'}
    ]
    Menu(opciones=[{'text':'Primero', 'command':partial(Ingresar_Datos,lista=formulario, botones=botones)}])