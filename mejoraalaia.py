# -*- coding: utf-8 -*-
"""MejoraalaIA.ipynb

Original file is located at
    https://colab.research.google.com/drive/1wjcUzmecB5xxGDxEQnSUpS4Y2spXjAsw
"""
def crear_tablero():
    tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    return tablero

def imprimir_tablero(tablero):
        print(f"{tablero[0][0]}|{tablero[0][1]}|{tablero[0][2]}")
        print("-----")
        print(f"{tablero[1][0]}|{tablero[1][1]}|{tablero[1][2]}")
        print("-----")
        print(f"{tablero[2][0]}|{tablero[2][1]}|{tablero[2][2]}")



def movimiento_jugador(tablero, jugador):
    while True:
        try:
            fila = int(input("Elige fila (0, 1, 2): "))
            columna = int(input("Elige columna (0, 1, 2): "))
            if 0 <= fila <= 2 and 0 <= columna <= 2:
                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador
                    break
                else:
                    print("¡Casilla ocupada!")
            else:
                print("¡Entrada inválida! Por favor, elige una fila y columna entre 0 y 2.")
        except ValueError:
            print("¡Entrada inválida! Por favor, ingresa números.")


def hay_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True

    return False


def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

import random

def evaluar_movimiento(tablero, fila, columna, jugador):
    """Evaluates a potential move for the given player."""
    oponente = "X" if jugador == "O" else "O"


    tablero[fila][columna] = jugador
    if hay_ganador(tablero):

        tablero[fila][columna] = " "
        return 10


    tablero[fila][columna] = " "


    tablero[fila][columna] = oponente
    if hay_ganador(tablero):

        tablero[fila][columna] = " "
        return 5


    tablero[fila][columna] = " "

    return 1


def movimiento_ia(tablero):
    casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    mejores_movimientos = []
    mejor_puntuacion = -float('inf')

    for fila, columna in casillas_vacias:
        puntuacion = evaluar_movimiento(tablero, fila, columna, "O")
        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
            mejores_movimientos = [(fila, columna)]
        elif puntuacion == mejor_puntuacion:
            mejores_movimientos.append((fila, columna))

    if mejores_movimientos:
        fila, columna = random.choice(mejores_movimientos)
        tablero[fila][columna] = "O"


def juego_completo():
    player_wins = 0
    ai_wins = 0

    while True:
        tablero = crear_tablero()
        jugador_actual = "X"
        juego_terminado = False

        while not juego_terminado:
            imprimir_tablero(tablero)
            print(f"Turno de {jugador_actual}")
            if jugador_actual == "X":
                movimiento_jugador(tablero, jugador_actual)
            else:
                movimiento_ia(tablero)


            if hay_ganador(tablero):
                imprimir_tablero(tablero)
                print(f"¡{jugador_actual} ha ganado!")
                if jugador_actual == "X":
                    player_wins += 1
                else:
                    ai_wins += 1
                juego_terminado = True
            elif tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print("¡Empate!")
                juego_terminado = True
            else:
                if(jugador_actual=="O"):
                    jugador_actual="X"
                else:
                    jugador_actual = "O"

        print(f"Marcador: Jugador (X): {player_wins} - IA (O): {ai_wins}")

        while True:
            jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
            if jugar_de_nuevo in ["s", "n"]:
                break
            else:
                print("Respuesta inválida. Por favor, ingresa 's' o 'n'.")

        if jugar_de_nuevo == "n":
            break

juego_completo()
