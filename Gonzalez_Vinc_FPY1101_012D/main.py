from os import system
from msvcrt import getch
from funciones import *

try:

    while True:
        print("Presione una tecla para continuar")
        getch()
        system("cls")
        print("""
                1. Stock marca
                2. Busqueda por precio
                3. Actualizar precio
                4. Salir """)

        seleccion=int(input("seleccione una opcion : "))


        if seleccion==1:
            print("Ah seleccionado stock marca")
            marca=input("Ingrese la marca : ")
            stock_marca(marca)
        elif seleccion==2:
            print("Ah seleccionado Busqueda por precio ")
            p_min=input("ingrese el valor minimo : ")
            p_max=input("ingrese el valor maximo : ")
            búsqueda_precio(p_min,p_max)
        elif seleccion == 3:
            print("Ah seleccionado actualizar precio ")
            clave=input("ingrese la clave del producto : ")
            actualizar_precio()
        elif seleccion== 4:
            break
        else:
            print("seleccion no valida")

except:
    print("Ah ocurrido un error")


    
    
