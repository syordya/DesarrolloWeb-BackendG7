'''
EJERCICIO 6

Ingresar numeros hasta que ese numero sea adivinado

    > numero_adivinar = 10
    > 5 => 'el numero es mayor que ese'
    > 13 => 'el numero es menor que ese'
    > 10 => 'felicidades adivinaste el numero'
    
'''

num = int(input("Ingrese numero para adivinar: "))
numero_magico=10
while num != numero_magico:
    if num > numero_magico:
       print("el numero es mayor que el Numero Magico")
    elif num < numero_magico:
        print("el numero es menor que el Numero Magico")
    num =int(input("Ingrese numero ah adivinar: "))
print("Felicitaciones adivinaste el numero")