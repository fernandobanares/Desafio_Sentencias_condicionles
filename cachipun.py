import random

jugada = str(input("ingrese su jugada (piedra, papel o tijera): ")).lower()

lista = ["piedra", "papel", "tijera"]


def cachipun():
    if random.choice(lista) == jugada:
        print("Es un empate")
    elif jugada == "piedra" and random.choice(lista) == "papel":
        print("Tu jugaste piedra \nComputadora jugó papel \nGana la computadora!!")
    elif jugada == "piedra" and random.choice(lista) == "tijera":
        print("Tu jugaste piedra \nComputadora jugó tijera \nGanaste!!")
    elif jugada == "papel" and random.choice(lista) == "piedra":
        print("Tu jugaste papel \nComputadora jugó piedra \nGanaste!!")
    elif jugada == "papel" and random.choice(lista) == "tijera":
        print("Tu jugaste papel \nComputadora jugó tijera \nGana la computadora!!")
    elif jugada == "tijera" and random.choice(lista) == "piedra":
        print("Tu jugaste papel \nComputadora jugó piedra \nGana la computadora!!")
    elif jugada == "tijera" and random.choice(lista) == "papel":
        print("Tu jugaste papel \nComputadora jugó piedra \nGanaste!!")
    else:
        print("Argumento inválido: Debe ser piedra, papel o tijera.")

cachipun()
