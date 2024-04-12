import numpy as np

def iniciar_tablero(size = (10, 10), fill = " "):

    tablero = np.full(size, fill)
    return tablero


iniciar_tablero()

tablero_inicial = iniciar_tablero()


barcos = {
    
    "b1_1" : [[2,2]],
    "b1_2" : [[3,5]],
    "b1_3" : [[6,9]],
    "b1_4" : [[8,9]],
    "b2_1" : [[4,2], [4,3]],
    "b2_2" : [[3,9], [3,10]],
    "b2_3" : [[8,6], [8,7]],
    "b3_1" : [[2,7],[3,7],[4,7]],
    "b3_2" : [[9,2], [9,3],[9,4]],
    "b4_1" : [[6,4], [6,5], [6,6], [6,7]]
} 

def colocar_barcos(tablero, barcos):
    for barco in barcos:
        for posicion in barcos[barco]:
            x,y = posicion
            tablero[x-1,y-1] = "0"
    return tablero

tablero_barcos = colocar_barcos(tablero_inicial, barcos)

print(tablero_barcos)

disparos = []

def disparar():
    disparo_x = int(input("Coord X : "))
    disparo_y = int(input("Coord Y : "))

    if tablero_barcos[disparo_x-1, disparo_y-1] == "O":
        tablero_barcos[disparo_x-1, disparo_y-1] = "X"
        print("¡Has acertado!")
        # Aquí puedes agregar lógica para verificar si el barco está tocado o hundido.
    elif tablero_barcos[disparo_x-1, disparo_y-1] == " ":
        tablero_barcos[disparo_x-1, disparo_y-1] = "-"
        print("Agua.")
    else:
        print("Ya has disparado aquí antes.")

    print(tablero_barcos)

disparar()
