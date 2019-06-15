
# Definir una funcion con un valor por defecto
def saludo(nombre = "Usuario"):
    print ("Hola, " + nombre)


saludo("Lemuri")
saludo("Karen")
saludo()

#funcion retornar la suma de dos numeros
def suma(numero_uno, numero_dos):
    return numero_uno + numero_dos

print(suma(45,15))

#funcion lambda o anonima, se define en una sola linea
multiplica = lambda numero_uno, numero_dos: numero_uno * numero_dos

print(multiplica(5,3))
