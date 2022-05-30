def delete_barran(list):
    for linea in range(len(list)):
        palabra = list[linea]
        lista2.append(palabra.replace("\n", ""))
    return lista2


lista2 = []
file = open("nombre_archivo.txt","w")
file.write("Hola clase \n")
file.close()

file = open("nombre_archivo.txt","a")
file.write("Adios clase")
file.close()

file = open("nombre_archivo.txt","r")
lista = (file.readlines())
file.close()

print(lista)
print(delete_barran(lista))
