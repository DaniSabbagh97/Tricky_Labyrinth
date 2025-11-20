# -----------------------------
# MINI-PROYECTO: LABERINTO SIMPLE
# -----------------------------
def imprimir_laberinto(lab):
    for fila in lab:
        linea = ""
        for elemento in fila:
            linea = linea + str(elemento) + " "
        print(linea)
    print()  

# Laberinto: 1 = pared, 0 = camino, P = jugador
lab = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, "P", 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]


# Posición inicial del jugador
pos_i, pos_j = 2, 2

# Diccionario de direcciones
movs = {
    "w": (-1, 0),  # arriba
    "s": (1, 0),   # abajo
    "a": (0, -1),  # izquierda
    "d": (0, 1)    # derecha
}

print("Laberinto inicial:")
imprimir_laberinto(lab)
jugando = True

while jugando:
    mov = input("Mover (w/a/s/d) o 'q' para salir: ")

    # Caso salir
    if mov == "q":
        print("Juego terminado.")
        jugando = False
    else:
        try:
            # Intentar obtener el desplazamiento (si no existe la tecla → KeyError)
            di, dj = movs[mov]
            movimiento_valido = True
        except KeyError:
            movimiento_valido = False

        if movimiento_valido:
            # Calcular nueva posición
            ni = pos_i + di
            nj = pos_j + dj

            # Verificar si hay pared
            choca_pared = (lab[ni][nj] == 1)

            if not choca_pared:
                # Mover jugador
                lab[pos_i][pos_j] = 0
                lab[ni][nj] = "P"
                pos_i, pos_j = ni, nj
                imprimir_laberinto(lab)
            else:
                print("¡No puedes pasar! Hay una pared.")
        else:
            print("Movimiento no válido.")


