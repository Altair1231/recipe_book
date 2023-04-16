
archivo = open("mi_archivo.txt","w")


archivo.write("Nuevo Texto")

archivo.close()

archivo = open("mi_archivo.txt")

print(archivo.read())

archivo.close()

