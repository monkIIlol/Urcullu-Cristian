from os import system
system('cls')
import os 
import csv
import math
lista = []
comunas = ("Concepción","Chiguayante","Talcahuano","Hualpén","San Pedro")

def registrar_pedido():

    
    registro = []
    cont6 = 0
    cont10 = 0
    cont20 = 0
    vueltas = 0

    while True:
        nombre = input("""
Ingrese su Nombre: """)
        
        if nombre.isalpha():
            registro.append(nombre)
            break

    while True:
        apellido = input("""
Ingrese su Apellido: """)

        if apellido.isalpha():
            registro.append(apellido)
            break
    while True:
        comuna = input("""
Ingrese su comuna: """)
        
        if comuna != "" or comuna != " ":
            registro.append(comuna)
            break

    while True:

        if vueltas >= 3:
            break

        elección_litros = input(f"""


¿Qué tipos de cilindros desea comprar?

1. 6 Litros
2. 10 Litros
3. 20 Litros""")
        
        if elección_litros == "1":
            cont6 += 1
            vueltas += 1

        elif elección_litros == "2":
            cont10 += 1
            vueltas += 1

        elif elección_litros == "3":
            cont20 += 1
            vueltas += 1

        else:
            print("Ingrese un valor correcto...")

        while True:
            siono = input("""
¿Desea elegir más tipos de cilindros?

1. Si
2. No""")
        
            
            if siono == "1":
                break

            elif siono == "2":
                break

        if siono == "1":
            continue

        elif siono == "2":
            break

    if cont6 > 0:
        while True:
            cant6 = input("""
Ingrese cantidad de cilindros de 6 Lts: """)
            if cant6.isnumeric():

                int6 = int(cant6)
                cont6 = int6
                registro.append(cont6)
                break
    else:
        registro.append(cont6)

    if cont10 > 0:
        while True:
            cant10 = input("""
Ingrese cantidad de cilindros de 10 Lts: """)
            if cant10.isnumeric():

                int10 = int(cant10)
                cont10 = int10
                registro.append(cont10)
                break
    else:
        registro.append(cont10)

    if cont20 > 0:
        while True:
            cant20 = input("""
Ingrese cantidad de cilindros de 20 Lts: """)
            if cant20.isnumeric():

                int20 = int(cant20)
                cont20 = int20
                registro.append(cont20)
                break
    else:
        registro.append(cont20)

    lista.append(registro)
    print(lista)
    for elem in lista:
            print(f""" 
DETALLE
          
ID del pedido          Cliente          Sector          Disp 6LTS          Disp 10LTS          Disp 20LTS
                {elem[0]} {elem[1]}             {elem[2]}                {str(elem[3])}                  {str(elem[4])}                        {str(elem[5])}""")
#registrar_pedido()

def listar():
    print("""
ID del pedido          Cliente          Sector          Disp 6LTS          Disp 10LTS          Disp 20LTS
""")

    for elem in lista:
        print(f"""
                {elem[0]} {elem[1]}             {elem[2]}                {str(elem[3])}                  {str(elem[4])}                        {str(elem[5])}""")

def imprimir():
    pass
def buscar():
    pass


while True:
    op = input("""
elija opción
           
1. Registrar pedido
2. Listar los pedidos
3. Imprimir hoja de ruta
4. Buscar un pedido por ID
5. Salir""")

    match op:

        case "1":
            registrar_pedido()

        case "2":
            listar()

        case "5":
            break