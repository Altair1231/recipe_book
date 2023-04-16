


def abrir_leer(archivo):
    return archivo.read()

documento = open("texto2.txt")

print(abrir_leer(documento))

documento.close()