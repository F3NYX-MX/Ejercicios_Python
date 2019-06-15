
myStr = "Hola, Mundo Feliz"
myName = "Lemuri"
# print(dir(myStr))  imprime todos los metodos que se pueden aplicar a la variable String

print(myStr.upper())
print(myStr.lower())
print(myStr.capitalize())
print(myStr.swapcase())

print(myStr.replace(',',';'))

#metodos encadenados, reemplazas y despues convertir a mayusculas.
print(myStr.replace(', ','').upper())


print(myStr.count(','))     #cuantos caracteres aparecen en la cadenna

print(myStr.startswith('Hola'))     #Inicia con hola? true o false

print(myStr.endswith('o'))          #Termina con o? true o false

print(myStr.split(','))         #separar en cadenas, cada vez q encuentre una coma

print(myStr.split())            #separar en cadenas, cada vez q encuentre un espacio en blanco

print(myStr.find('o'))          #Buscar el caracter, si existe, devuelve la posicion
print(myStr.index('M'))         #devuelde la posicion del caracter indicado
print(myStr[3])                 #devuelve el caracter en la posicion indicada

print(len(myStr))               #Tamaño de la cadena

print("Mi nombre es {0}, y mi libro favorito se llama: {1}".format(myName,myStr))

