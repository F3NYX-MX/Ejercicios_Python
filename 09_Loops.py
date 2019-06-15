
mi_lista = ["Leche","Jamon","Queso","Catsup","Manzanas","Pastel","Avena"]

for item in mi_lista:
    if item == "Queso":
        continue
    if item == "Pastel":
        break
    print(item)


contador = 1
while contador <= 10:
    print(contador)
    contador = contador + 1
    