'''
EJERCICIO 2

Escribir el codigo que el usuario le ingrese el grosor de un octagono y que lo dibuje
Ejemplo:

> Grosor : 5

       *****
      *******
     *********
    ***********
   *************
   *************
   *************
   *************
   *************
    ***********
     *********
      *******
       *****

'''

grosor = int(input('Ingrese el grosor: '))

altura = grosor + 2*(grosor-1)
fila = grosor
espacio = grosor - 1 #3

for i in range(1,altura + 1): 
    if(i < grosor):
        print(" " * espacio, end = "")
        for j in range(fila):
            print("*", end = "")
        fila += 2
        espacio -= 1

    if(i >= grosor and i<= (grosor + grosor -1 )):
        for j in range(fila):
            print("*", end = "")
        espacio = 0        

    if(i > (grosor + grosor -1 )):
        fila -= 2
        espacio += 1
        print(" " * espacio, end = "")
        for j in range(fila):
            print("*", end = "")        
    print()