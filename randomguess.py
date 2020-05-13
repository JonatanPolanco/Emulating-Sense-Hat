 import random

print("adivina el número")
intentos=0

aleatorio= random.randint(1,20)
print("el número está entre 1 y 20")
print("tienes 3 intentos, buena suerte")

while intentos<=3
    print("cuál crees que es?")
    numero=input()
    numero=int(numero)
    
    if numero!=aleatorio:
        print("incorrecto, intenta de nuevo")
        
    if numero==aleatorio:
        print("acertaste!")
        
    intentos=intentos+1
break
    
