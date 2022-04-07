paranoid_android = "Marvin, the paranoid android"
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t', char)
print()    
#la multiplicacion *2 es para hacer desplazamientos horizontales de la palabra
#*2 inserts 2 tab characters before each printed object.
for char in letters[-7:]:
    print('\t'*2, char)
print()    

for char in letters[12:20]:
    print('\t'*3, char)
print()

'''imprimir parte de la lista.'''
print(letters[:6])
print(letters[-1])
