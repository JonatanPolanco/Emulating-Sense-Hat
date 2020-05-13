import random

print("adivina el número")
intentos=0

aleatorio= random.randint(1,20)
print("el número está entre 1 y 20")
print("tienes 3 intentos, buena suerte")

for intentos in range(0, 4):
    if intentos==3:
        print("perdiste ;(")
        break
    print("cuál crees que es?")
    numero=input()
    numero=int(numero)
    intentos=intentos+1

    if numero!=aleatorio:
        print("incorrecto, intenta de nuevo")

    if numero==aleatorio:
        print("acertaste!")
        break