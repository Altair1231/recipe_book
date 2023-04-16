



def registro_error(archivo):

    documento = open(archivo,"a")
    documento.writelines("se ha registrado un error de ejecución")
    documento.close()

