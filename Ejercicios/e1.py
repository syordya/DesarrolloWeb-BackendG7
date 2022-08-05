'''
EJERCICIO 1 

Escriba el codigo que le pida al usuario ingresar la altura y el ancho de un rectangulo y
que lo dibuje usando *, ejemplo:

 > altura: 5
 > ancho: 4

Resultado:

                ****
                ****
                ****
                ****
                ****

'''

altura = int(input("Ingrese la altura: "))
ancho = int(input('Ingrese el ancho: '))

for i in range (altura):
    for j in range (ancho):
        print('*', end="")
    print("")