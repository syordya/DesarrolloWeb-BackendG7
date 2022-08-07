'''
Funcion que retorna una cadena de texto
enviada en formato camelcase
'''

def newCamelCase(text = ''):
    x = text.split()
    nuevo = ""
    for palabra in x:
            if palabra == 'a' or palabra == 'is':
                    nuevo  += " "+palabra
                    continue
                    
            nuevo += " "+palabra.title()
    return nuevo.strip()



txt = "es un placer llevar el curso de backend"

print(newCamelCase(txt))