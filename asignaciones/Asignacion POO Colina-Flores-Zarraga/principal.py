import funciones
import pantallas
from functools import partial

#--------------------------------------------
#Funciones especificas de programa 
#--------------------------------------------
def Datos():
    global ingresar, nuevo
    ingresar , nuevo = pantallas.Ingresar_Datos(lista=formulario, botones=botones)

def Mostrar():
    
    pantallas.Mostrar_Datos(lista=formulario, datos = Estudiantes)

def Guardar():
    global nuevo, Estudiantes
    data = {}
    for dato in nuevo:
        data[dato['label']] = dato['input'].get()

    Estudiantes.append(data)
    funciones.GuardaArchivo(Estudiantes)
    
    ingresar.destroy()

#--------------------------------------------
#Variables del programa
#--------------------------------------------
Estudiantes=funciones.LeerArchivo()
nuevo=[]
ingresar=None

#--------------------------------------------
#Formulario para e ingreso de datos
#--------------------------------------------
formulario=[
        {'label':'Cedula'},
        {'label':'Nombre'},
        {'label':'Apellido'},
        {'label':'Direccion'},
        {'label':'Telefono'},

]
botones = [{'text': 'Guardar', 'command':Guardar},
]

#--------------------------------------------
#Menu principal del sistema
#--------------------------------------------
opciones=[
    {'text':'Ingresar datos', 'command':Datos},#partial(pantallas.Ingresar_Datos, lista=formulario, botones=botones)},
    {'text':'Mostrar datos', 'command':Mostrar},
    {'text':'Buscar datos', 'command':pantallas.abrir_ventana_secundaria},
    {'text':'Eliminar datos', 'command':pantallas.abrir_ventana_secundaria},
    {'text':'Modificar datos', 'command':pantallas.abrir_ventana_secundaria},
    {'text':'Ordenar datos', 'command':pantallas.abrir_ventana_secundaria},

]


if __name__ == "__main__":
    Patalla = pantallas.Menu(opciones=opciones)