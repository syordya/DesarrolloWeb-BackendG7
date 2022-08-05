'''
EJERCICIO 4

Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
 > si el numero es par, se divide entre dos
 > si el numero es impar, se multiplica por 3 y se suma 1
la serie termina cuando el numero es 1

Ejemplo : 19

    19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
    
'''


numero = int(input("Ingrese un número: "))
resultado = numero
series =[]
series.append(numero)

while resultado != 1:
    if(resultado%2==0):
        resultado = resultado // 2
        series.append(resultado)
    else:
        resultado = resultado*3 + 1
        series.append(resultado)

print(series)