
tamaño = 100
#primeros dos valores
x = 0
y = 1
iteracion = 0
if tamaño <= 0:
   print("Ingrese un número mayor a cero")
elif tamaño == 1:
   print("Esta secuencia Fibonacci tiene {} elementos".format(tamaño), ":")
   print(x)
else:
   
   print("Esta secuencia Fibonacci tiene {} elementos".format(tamaño), ":")
   while iteracion < tamaño:
       print(x, end=",")
       z = x + y
       x = y
       y = z
       iteracion += 1
      