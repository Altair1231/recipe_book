

archivo = open("mi_archivo2.txt","a")

archivo.write("Nuevo inicio de sesión\n")

archivo.close()

archivo = open("mi_archivo2.txt")

print(archivo.read())

archivo.close()