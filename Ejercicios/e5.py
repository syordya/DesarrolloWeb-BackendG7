'''
EJERCICIO 6

Si el texto de ingreso es:

    > texto = "hola alumnos buenas noches ya se viene el break"

 entonces el texto resultado debera ser:

    resultado_final = ["Hola", "Alumnos", "Buenas", "Noches", "Ya", "Se"]

'''

texto = input("Ingresar el texto: ")
lista = texto.split(" ")
print([" , ".join(lista)])