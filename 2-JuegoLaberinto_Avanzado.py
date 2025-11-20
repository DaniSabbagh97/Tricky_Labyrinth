def imprimir_laberinto(lab):
    for fila in lab:
        for elemento in fila:
            print(str(elemento), end=" ")
        print()
    print()


# -----------------------------
# LABERINTOS DE DIFERENTES NIVELES
# -----------------------------

lab_nivel_1 = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,"P",0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,0,0,1,1,0,1,0,1],
    [1,1,1,0,1,0,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,1,0,0,0,"S",1],
    [1,1,1,1,1,1,1,1,1,1],
]

lab_nivel_2 = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,"P",0,1,0,0,0,1,0,1],
    [1,0,0,1,0,1,0,1,0,1],
    [1,1,0,0,0,1,0,0,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1,1],
    [1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,"S",1],
    [1,1,1,1,1,1,1,1,1,1],
]

lab_nivel_3 = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,"P",0,0,0,1,0,0,0,1],
    [1,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,1,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,0,1,1,1,"S",1],
    [1,1,1,1,1,1,1,1,1,1],
]


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

# Posición inicial fija (todos comienzan en [1][1])
pos_i = 1
pos_j = 1


# -----------------------------
# JUEGO
# -----------------------------

movs = {
    "w": (-1, 0), 
    "s": (1, 0),  
    "a": (0, -1),
    "d": (0, 1)
}

jugando = True

print("\n¡Llega a la S para ganar!\n")
imprimir_laberinto(lab)

while jugando:
    mov = input("Mover (w/a/s/d) o 'q' para salir: ")

    if mov == "q":
        print("Juego terminado.")
        jugando = False
    else:
        # Validación del movimiento SIN usar 'in'
        try:
            di, dj = movs[mov]
            movimiento_valido = True
        except KeyError:
            movimiento_valido = False

        if movimiento_valido:
            ni = pos_i + di
            nj = pos_j + dj

            if lab[ni][nj] != 1:  # si no es pared
                if lab[ni][nj] == "S":
                    lab[pos_i][pos_j] = 0
                    lab[ni][nj] = "P"
                    imprimir_laberinto(lab)
                    print("¡HAS GANADO!")
                    jugando = False
                else:
                    lab[pos_i][pos_j] = 0
                    lab[ni][nj] = "P"
                    pos_i, pos_j = ni, nj
                    imprimir_laberinto(lab)
            else:
                print("¡Hay una pared!")
        else:
            print("Movimiento no válido.")
