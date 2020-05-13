def revertir(palabra):
    largo=len(palabra)
    mitad=int(largo/2)
    palabra1= palabra[:mitad]
    palabra2= palabra[mitad:]
   
    print(palabra2+palabra1)
    
texto= input("ingrese el texto :  ")
x=revertir(texto)