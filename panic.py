phrase = "Don't panic!"

plist = list(phrase)

print(phrase)

print(plist)

#con el for se sacan las ultimas 4 letras de la variable phrase
for i in range(4):
    plist.pop()

plist.pop(0)
plist.remove("'")

#cambia lo posiscion de los ultimos dos valores
plist.extend([plist.pop(), plist.pop()])

#se inserta en la  posicion 2 lo que se extrae del espacio 3 de la lista.
#cuando se usa insert no reemplaza el valor que se encuentra en el lugar 2
#lo unico que hace es desplazar a la derecha el valor que ahi se encontraba.
plist.insert(2, plist.pop(3))

#junta las letras sueltas, es decir convierte los valores en un string
new_phrase = ''.join(plist)

print(plist)

print(new_phrase)
