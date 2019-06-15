#leer un valor del teclado y sumarle una cantidad

age = input("Insert your age: ")
print(age)
print(type(age))    #age es de tipo string al leerse del teclado

age = int(age) + 5  #convertir age a entero, para poder sumar

print(age)
