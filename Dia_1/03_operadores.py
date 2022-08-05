# Operadores Aritmeticos

edad_juan_diego = 50
edad_karime = 18

# SUMA - ADICION
print(edad_juan_diego + edad_karime)

# RESTA - SUSTRACCION
print(edad_juan_diego - edad_karime)

# MULTIPLICACION - PRODUCTO
print(edad_juan_diego * edad_karime)

# DIVISION 
print(edad_juan_diego / edad_karime)

# MODULO
print(edad_juan_diego % edad_karime)

# COCIENTE 
print(edad_juan_diego // edad_karime)

# POTENCIA
print(edad_juan_diego ** 1)

# print("{} - {}".format(20,19))
# En el caso de los caracteres Strings
# cuando hacemos una sumatoria en los String se hara una concatenacion
mes = 'Junio'
temporada = 'invierno'
print(mes + temporada)
# y si hacemos uso de la multiplicacion hara que se repita N cantidad de veces
print(mes * 5)


# -------------------------------------------

# Operadores Comparacion

edad_holden = 15
edad_taylor = 30

# >  Mayor que 
print(edad_holden > edad_taylor)

# < Menor que
print(edad_holden < edad_taylor)

# == Igual que
print(edad_holden == edad_taylor)

# != Diferente que
print(edad_holden != edad_taylor)

# >= Mayor o igual que
print(edad_holden >= edad_taylor)

# <= Menor o igual que
print(edad_holden <= edad_taylor)


# Operadores Logicos

edad_drake = 25
edad_taylor = 30

# and Y > basta con que una de las dos condiciones sea F para que todo sea F
print(edad_drake > 18 and edad_drake > edad_taylor)
# or O > basta con que una sea V para que todo sea V
print(edad_drake > 18 or edad_drake > edad_taylor)
# not NO > invierte el resultado
print(not edad_drake > 50)


# Ejercicios
edad_eduardo= 18
edad_fabio = 26
edad_fatima = 35


# Como saber si eduardo es mayor de edad
print(edad_eduardo >= 18)

# Como saber si eduardo es mayor que fatima
print(edad_eduardo > edad_fatima)

# Como saber si fabio es menor que fatima pero mayor que eduardo
print(edad_fabio < edad_fatima and edad_fabio > edad_eduardo)

# como saber si fatima puede ser mayor que fabio o menor que eduardo
print(edad_fatima > edad_fabio or edad_fatima < edad_eduardo)


# Operadores de Asignacion
# = Asignacion
edad = 50

# += Incremento
edad += 1 # edad++

# -= Decremento
edad -= 1 # edad--

# *= Multiplicador
edad *= 1

# /= Division
edad /= 2