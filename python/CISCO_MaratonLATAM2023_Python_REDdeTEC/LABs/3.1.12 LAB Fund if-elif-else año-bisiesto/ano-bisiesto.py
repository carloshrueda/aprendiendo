"""
Escenario
Como seguramente sabrás, debido a algunas razones astronómicas, el año puede ser bisiesto o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

si el número del año no es divisible entre cuatro, es un año común.
de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
de lo contrario, si el número del año no es divisible entre 400, es un año común.
de lo contrario, es un año bisiesto.
"""
ano = int(input("Ingrese un año? "))

# if ano < 1582:
#    print("No dentro del período del calendario gregoriano")
# elif ano % 4 != 0:
#    print("Comun")
# elif ano % 100 != 0:
#    print("Bisiesto")
# elif ano % 400 != 0:
#    print("Comun")
# else:
#    print("Bisiesto")

if ano < 1582:
   print("No dentro del período del calendario gregoriano")
elif (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
   print("Bisiesto")
else:
   print("Comun")


