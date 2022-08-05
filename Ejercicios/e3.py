'''
EJERCICIO 3

De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
invertido

 > Ejemplo

   Altura: 4
        ****
        ***
        **
        *

'''

altura = int(input("Ingrese la altura: "))

for i in range(1, altura + 1):
    for j in range(1, altura + 1):
        print("*", end = "")
    altura -=1    
    print()