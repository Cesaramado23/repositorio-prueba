from os import system
import json
class Funciones:


    #Función utilizada para el ingreso de los datos
    # con la ayuda de los keys del diccionario estudiante 
    def IngresarDatos1():
        estudiante={'CI':'', 'Nombre': '', 'Apellido':'', 'Telefono':'', 'Direccion':''}
        print('Ingresar Datos')
        for entrada in estudiante.keys():
            estudiante[entrada] = input(entrada+': ')
        estudiante['Materias']= []
        return estudiante


    def MostrarDatos(Estudiantes):
        system("cls")
        print('-----------------Lista de Estudiantes-------------------')
        for data in Estudiantes:
            print('Cedula:', data['CI'], 'Nombre: ',data['Nombre'], 'Apellido: ',data['Apellido'])


    # Muestra los datos que se encuentran en la lista Estudiantes
    # Recorre la lista Estudiantes con un for para mostrar CI, Nombre, Apellido de cada uno de los registros encontrados en la lista
    # Función de búsqueda que permite ubicar por CI la posición de un registro
    # si CI no es encontrada la búsqueda da como salida -1, 
    # si se encuentra muestra los datos y el parámetro mostrar=True y devuelve la posición del registro

    def BuscarDatos(Estudiantes, mostrar=False):
        print('Buscar datos')
        system("cls")
        CI = input('Indique la cedula a bucar: ')
        pos=0
        posicion = -1
        for data in Estudiantes:
            if (data['CI']==CI):
                if (mostrar==True):
                    print('Cedula:', data['CI'], 'Nombre: ',data['Nombre'], 'Apellido: ',data['Apellido'])
                posicion=pos
                break
            pos=pos + 1
        return posicion
    

    # Función utilizada para eliminar un registro por medio de la CI
    # Si CI es encontrada muestra los datos y pregunta si quiere eliminar el usuario
    def EliminarDatos(Estudiantes):
        print('Eliminar datos')
        posicion = Funciones.BuscarDatos(Estudiantes)
        if (posicion != -1):
            r=input('Desea eliminar: '+ Estudiantes[posicion]['Nombre']+' '+Estudiantes[posicion]['Apellido']+' (s/N): ')
            if (r in ['s', 'S', 'y', 'Y', 'si', 'Si', 'SI']):
                Estudiantes.pop(posicion)
                print('---------------El usuario fue eliminado---------')
            else:
                print('---------------El usuario no fue eliminado---------') 
        else:
            print('---------------El usuario no existe---------')
        return Estudiantes
    # Busca el registro por medio de la CI, si es encontrado pregunta si desea modificarlo
    # Si selecciona modificar el Sistema le muestra el valor de cada campo, si escribimos un nuevo valor es agregado a dicho campo, 
    # de lo contrario si solo presionamos enter el campo mantiene su valor anterior
    def ModificarDatos(Estudiantes):
        print('Modificar datos')
        posicion = Funciones.BuscarDatos(Estudiantes)
        if (posicion != -1):
            r=input('Desea Modificar: '+ Estudiantes[posicion]['Nombre']+' '+Estudiantes[posicion]['Apellido']+' (s/N): ')
            if (r in ['s', 'S', 'y', 'Y', 'si', 'Si', 'SI']):  
                for campo in Estudiantes[posicion].keys():
                    nuevo = input(campo+ ' : (' + str(Estudiantes[posicion][campo])+'): ')
                    if (nuevo!=''):
                        Estudiantes[posicion][campo]=nuevo    
                print('---------------El usuario fue Modificado---------')
            else:
                print('---------------El usuario no fue Modificado---------') 
        else:
            print('---------------El usuario no existe---------')
        return Estudiantes

    #Con esta función ordenamos el listado por cualquiera de los campos seleccionados por el usuario
    def OrdenarDatos (Estudiantes):
        system("cls")
        print('----------Ordenar Datos--------')
        cont = 0
        for campo in Estudiantes[0].keys():
            cont +=1
            print(campo,': ')
        r= input('Indique el campo a ordenar: ')
        if (r in Estudiantes[0].keys()):
            Estudiantes= sorted(Estudiantes, key=lambda estudiante : estudiante[r])
        Funciones.MostrarDatos(Estudiantes)
        return Estudiantes

    
    # Función que lee el archivo datos.json
    # Utilizamos try y except FileNotFoundError, para evitar que el programa inicie así exista o no datos.json
import sys

def LeerArchivo():
    try:
        with open('datos.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        sys.exit('El archivo datos.json no existe')

    # Función que Guarda los nuevos datos en el archivo datos.json
    def GuardaArchivo(datos):
        with open('datos.json','w') as file:
            json.dump(datos, file, indent=4)








