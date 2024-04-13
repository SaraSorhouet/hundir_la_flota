import numpy as np

NUMERO_INTENTOS = 5

# dejo que el tablero sea de 10 por 10

def iniciar_tablero(size=(10, 10), fill=" "):
    return np.full(size, fill)

# future work, que la posicion de los barcos sea aleatoria
barcos = {
    "b1_1": [[2, 2]],
    "b1_2": [[3, 5]],
    "b1_3": [[6, 9]],
    "b1_4": [[8, 9]],
    "b2_1": [[4, 2], [4, 3]],
    "b2_2": [[3, 9], [3, 10]],
    "b2_3": [[8, 6], [8, 7]],
    "b3_1": [[2, 7], [3, 7], [4, 7]],
    "b3_2": [[9, 2], [9, 3], [9, 4]],
    "b4_1": [[6, 4], [6, 5], [6, 6], [6, 7]]
}
