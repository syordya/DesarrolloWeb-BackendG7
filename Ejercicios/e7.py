'''
EJERCICIO 7

Dado los siguientes numeros:

    > numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]

Indicar cuantos de ellos son multiplos de 3 y de 5 , 
ademas si hay un multiplo de 3 y de 5 no contabilizarlos

Ejemplo : 

multiplos de 3: 4 , multiplos de 5: 1

'''
numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
cont_tres=0
cont_cinco=0
for i in numeros:
    if i%3==0 and i%5==0:
        continue
    elif i%3==0:
        cont_tres+=1
    elif i%5==0:
        cont_cinco+=1
print("los multiplos de 3 son: {} y los multiplos de 5 son: {}" .format(cont_tres,cont_cinco))