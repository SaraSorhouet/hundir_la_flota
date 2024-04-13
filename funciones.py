from variables import *

def mensaje_de_inicio():
    print("¡Bienvenido al juego de Hundir la Flota mas cutre del Mundo!")
    print("Tu objetivo es hundir todos los barcos del tablero")
    print("Hay 4 barcos de longitud 1 (b1_1, b1_2, b1_3, b1_4), 3 barcos de longitud 2 (b2_1, b2_2, b2_3)\n2 barcos de longitud 3 (b3_1, b3_2) y un barco de longitud 4(b4_1)).")
    print("Puedes disparar a una casilla del tablero especificando sus coordenadas.")
    print("Las coordenadas se especifican utilizando un numero del 0 al 10 para la coordenada X y un numero del 0 al 10 para la Coordenada Y")
    print(f"Tienes {NUMERO_INTENTOS} intentos para Hundir la Flota del Enemigo.")
    print("¡Buena suerte!\n")

def colocar_barcos(tablero, barcos):
    for barco in barcos:
        for posicion in barcos[barco]:
            x, y = posicion
            tablero[x - 1, y - 1] = "O"
    return tablero

def disparar(tablero_barcos, barcos, intentos):
    while True:
        try:
            disparo_x = int(input("Coord X : "))
            disparo_y = int(input("Coord Y : "))

            # las coordenadas son numericas por que introducir (A, J) es un lio 
            if disparo_x < 1 or disparo_x > 10 or disparo_y < 1 or disparo_y > 10:
                print("Coordenadas fuera de rango. Deben ser entre 1 y 10.")
                continue
            if tablero_barcos[disparo_x - 1, disparo_y - 1] == "X" or tablero_barcos[disparo_x - 1, disparo_y - 1] == "-":
                print("Ya has disparado aquí antes, lo siento")
                intentos -= 1  # Restar un intento por disparar en una posición ya disparada tanto si ha sido acierto o agua
                continue
            break
        except ValueError:
            print("Por favor, introduce SOLO números enteros del 1 al 10 para las coordenadas.")

    if tablero_barcos[disparo_x - 1, disparo_y - 1] == "O":
        tablero_barcos[disparo_x - 1, disparo_y - 1] = "X"
        print("¡Has acertado!")

        for barco, posiciones in barcos.items():
            for posicion in posiciones:
                if [disparo_x, disparo_y] == posicion:
                    print("¡Has tocado un barco!")
                    posiciones.remove(posicion)
                    if not posiciones:
                        print("¡El barco", barco, "ha sido hundido!")
        return intentos

    elif tablero_barcos[disparo_x - 1, disparo_y - 1] == " ":
        tablero_barcos[disparo_x - 1, disparo_y - 1] = "-"
        print("¡Oh, Lo siento! ¡Agua!")
        return intentos - 1  # Restar un intento si el disparo fue agua

