#listas


mi_lista = ["Lemuri","Colli","Saucedo",40,"Masculino"]
cColors = ['red','blue','green','black']
cvaloresRespuesta = [21,'Lemuri','Colli',[12,45,89]]

#Crear una lista con la funcion constructor list()
numbers_list = list((12,78,96,29))

print(numbers_list)

#definir una lista usando la funcion rango
rango = list(range(1,11))

print (rango)

#con la funcion dir() puedo ver todos los metodos que se pueden usar
#de un tipo de variable en particular
#print(dir(cColors))

#imprimir la posicion 0 de la lista de colores
print(cColors[0])

#obtener el primer elemento de la lista colors, pero en sentido inverso
print(cColors[-1])

#devuelve true, cuando existe el elemento en la lista
print('Colli' in mi_lista)

#Agregar un elemento a la lista, en la ultima posicion
cColors.append('violet')
print(cColors)

#Agregar varios elementos a la lista
cColors.extend(('Brown','pink'))
print(cColors)

#Insertar un elemento en la posicion deseada
cColors.insert(2,'orange')
print(cColors)

print('Tamaño de la lista')
print(len(cColors))

#Quitar el ultimo elemento
print('Quitar el último')
cColors.pop()
print(cColors)

#quitar el primer elemento que coincida con el parametro
print('Quitar el que tenga se llame red')
cColors.remove('red')
print(cColors)

#quitar todos los elementos de la lista
# print('Quitar todos los elementos')
# cColors.clear()
# print(cColors)

cColors.sort()
print(cColors)

#obtener el indice del elemento que se desea
print(cColors.index('violet'))

print('Contar las veces que aparece un elemento')
print(cColors.count('black'))