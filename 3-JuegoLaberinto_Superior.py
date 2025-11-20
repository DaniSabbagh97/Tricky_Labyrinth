import random

def imprimir_laberinto(lab):
    for fila in lab:
        linea = ""
        for elemento in fila:
            linea = linea + str(elemento) + " "
        print(linea)
    print()


# -----------------------------
# LABERINTO NIVEL 1 (con Monstruo)
# -----------------------------
lab_nivel_1 = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,"P",0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,1,"M",0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,0,0,1,1,0,1,0,1],
    [1,1,1,0,1,0,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,1,0,0,0,"S",1],
    [1,1,1,1,1,1,1,1,1,1],
]


# (Puedes añadir otros laberintos nivel 2 y 3 si quieres)
lab_nivel_2 = lab_nivel_1
lab_nivel_3 = lab_nivel_1


# -----------------------------
# SELECCIÓN DE NIVEL
# -----------------------------
nivel = input("Selecciona nivel (1, 2 o 3): ")

if nivel == "1":
    lab = lab_nivel_1
elif nivel == "2":
    lab = lab_nivel_2
elif nivel == "3":
    lab = lab_nivel_3
else:
    print("Nivel no válido. Se cargará el nivel 1 por defecto.")
    lab = lab_nivel_1

# Posición inicial
pos_i = 1
pos_j = 1

# Vidas
vidas = 3

# Movimientos
movs = {
    "w": (-1, 0),
    "s": (1, 0),
    "a": (0, -1),
    "d": (0, 1)
}

jugando = True

print("\n¡Llega a la S para ganar! Evita paredes. Tienes 3 vidas.")
print("Si pisas la M serás teletransportado.\n")
imprimir_laberinto(lab)

while jugando:
    print("Vidas restantes:", vidas)
    mov = input("Mover (w/a/s/d) o 'q' para salir: ")

    # Salida manual
    if mov == "q":
        print("Juego terminado.")
        jugando = False
    else:
        try:
            di, dj = movs[mov]
            movimiento_valido = True
        except KeyError:
            movimiento_valido = False

        if movimiento_valido:
            ni = pos_i + di
            nj = pos_j + dj

            casilla = lab[ni][nj]

            # -----------------------------
            # CHOQUE CONTRA PARED
            # -----------------------------
            if casilla == 1:
                vidas -= 1
                print("¡Has chocado contra una pared! Pierdes 1 vida.")

                if vidas == 0:
                    print("Te quedaste sin vidas. ¡Fin del juego!")
                    jugando = False

            # -----------------------------
            # SALIDA
            # -----------------------------
            elif casilla == "S":
                lab[pos_i][pos_j] = 0
                lab[ni][nj] = "P"
                imprimir_laberinto(lab)
                print("¡HAS GANADO!")
                jugando = False

            # -----------------------------
            # MONSTRUO (TELETRANSPORTE)
            # -----------------------------
            elif casilla == "M":
                print("¡Un monstruo te atrapó! Teletransporte aleatorio…")

                # Quitar jugador del sitio actual
                lab[pos_i][pos_j] = 0

                # Buscar posición aleatoria válida
                tele_i = 0
                tele_j = 0
                encontrada = False

                while not encontrada:
                    tele_i = random.randint(1, 8)
                    tele_j = random.randint(1, 8)

                    if lab[tele_i][tele_j] == 0:
                        encontrada = True

                lab[tele_i][tele_j] = "P"
                pos_i, pos_j = tele_i, tele_j

                imprimir_laberinto(lab)

            # -----------------------------
            # CASILLA NORMAL
            # -----------------------------
            else:
                lab[pos_i][pos_j] = 0
                lab[ni][nj] = "P"
                pos_i, pos_j = ni, nj
                imprimir_laberinto(lab)

        else:
            print("Movimiento no válido.")
