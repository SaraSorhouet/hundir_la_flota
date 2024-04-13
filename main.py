from variables import *
from funciones import *

mensaje_de_inicio()

tablero_barcos = colocar_barcos(iniciar_tablero(), barcos)

intentos = NUMERO_INTENTOS

while "O" in tablero_barcos and intentos > 0:
    print("Intentos restantes:", intentos)
    intentos = disparar(tablero_barcos, barcos, intentos)

if "O" not in tablero_barcos:
    print("¡Has hundido todos los barcos! Zorionak!")
else:
    print("Vaya, se te han acabado los intentos. ¡Fin del Juego!")
