
carrito_compra =  {
    "producto" : "Video juego",
    "cantidad" : 1,
    "precio"   : 45689.78
}

usuario = {
    "nombre" : "Lemuri Colli",
    "alias"  : "Fenyx",
    "edad"   : 41
}

usuario2 = {
    "nombre" : "Guillermo Colli",
    "alias"  : "RompeHuesos",
    "edad"   : 11
}

valores = {
    "Soledad"   : 35,
    "Lemuri"    : 41,
    "Guillermo" : 11,
    "Carlitos"  : 10,
    "Sofia"     :   9
}

#print(dir(usuario))
#print(type(usuario))
print(carrito_compra)
print(valores)
print(usuario.values())
print(usuario.keys())

#Actualizar el valor de un elemento
valores['Guillermo'] = 12

#imprimir el valor de un elemento
print(valores["Sofia"])

#Verificar si existe elemento 
print("Bertha" in valores)

#Agregar un nuevo elemento con su valor
valores["Timoteo"] = 60

#Asignar los dos diccionarios a una lista
lstLista = [usuario,usuario2]

print(lstLista)

