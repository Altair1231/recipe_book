


def sobrescribir(archivo):

    documento = open(archivo,"w")

    documento.write("Contenido Eliminado")
    return documento




sobrescribir("ejemplo.txt")


