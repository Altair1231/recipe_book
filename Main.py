# Bienvenida al usuario
# Le decimos al usuario donde se encentra la carpeta raiz de las recetas
# Cuantas recetas tiene en total recuerda el (**/*.txt)
# luego le vamos a dar a elegir entre 6 opciones
import os
import shutil
import sys
from os import system
from pathlib import Path

def recetas_totales(ruta):
    # Vamos a ver todos los archivos de recetas TXT que hay dentro del directorio
    total = []
    for recetas in ruta.glob("**/*.txt"):
        total.append(recetas)
    return total

print("Bienvenid@ a tu recetario personal!".upper())

ruta_raiz = Path.cwd()
ruta2 = Path("Recetas").resolve()


print(f"-Tu carpeta con todas tus recetas se encuentra en...{ruta_raiz}")

print(f"TIENES UN TOTAL DE '{len(recetas_totales(ruta2))}' RECETAS")

def menu ():
    print("\n[1] - Leer receta"
      "\n[2] - Crear receta"
      "\n[3] - Crear categoría"
      "\n[4] - Eliminar receta"
      "\n[5] - Eliminar categoría"
      "\n[6] - Finalizar programa")

menu()

numero = (input(f"\nELIGE UNA OPCIÓN: "))

def limpiar():
    os.system('clear')
def opcion_correcta(opcion):
    # Vamos a comprobar que lo que nos han pasado es un numero y que este entre el 1 y el 6(por hacer esto ultimo)
    lista_numeros_aceptados = ["1","2","3","4","5","6"]
    if opcion.isnumeric() and opcion in lista_numeros_aceptados:
        return True
    else:
        return False
def sacar_carpetas_numeradas():
    carpetas = []
    for carpeta in ruta2.glob("*"):
        carpetas.append(carpeta)
    # Limpiamos los resultados de carpetas
    for indice, valor in enumerate(carpetas):
        carpetas[indice] = valor.name
    # Impirimos los resultados con números
    for indice, valor in enumerate(carpetas, 1):
        print(f"[{indice}]-[{valor}]")
    print(f"\n[x]-[Volver al menú principal]")
    return carpetas



def principal(numero):
    while opcion_correcta(numero) == True:
        # Si te ha dado un numero del 1 al 6 comenzamos a hacer cosas:
        if numero == "1":  # Ver una receta
            # Procedemos a preguntar que categoría quiere seleccionar.
            limpiar()
            print(f"\n===SELECCIONA LA CATEGORÍA DESEADA=== \n")
            carpetas = sacar_carpetas_numeradas()
            seleccion1 = "a"  # Creamos esta variable con una letra para trigerear el while y que si o si le pases un numero y que este dentro del rango de carpetas
            # Comprobamos que es un numero y que no es mayor que el numero de carpetas
            seleccion1 = input("\nCATEGORÍA: ")
            if seleccion1 == "x":
                limpiar()
                os.execl(sys.executable, sys.executable, *sys.argv)
                pass
            else:
                pass
            while seleccion1.isnumeric() == False or int(seleccion1) > len(carpetas) or int(seleccion1) == 0:
                seleccion1 = input("\nCATEGORÍA: ")
                print("No es un numero o es mayor que el numero de carpetas")
            else:
                pass
            seleccion1 = carpetas[int(seleccion1)-1]  # Ahora seleccion1 es el nombre de la carpeta que ha escogido el usuario
            # Vamos a ver todos los archivos de recetas TXT que hay dentro del directorio
            total = []
            for recetas in ruta2.glob(f"{seleccion1}/*.txt"):
                total.append(recetas)
            # Limpiamos los resultados un poco y le añadimos un valor para poder usarlo despues
            escogida = []
            for indice,valor in enumerate(total):
                escogida.append(valor.name)

            limpiar()
            for indice,valor in enumerate(escogida,1):
                print(f"\n[{indice}]-[{valor}]")
            # Limpiamos los resultados un poco y le añadimos un valor para poder usarlo despues
            cual_leer = input(f"\nCUAL QUIERES LEER? ")
            if cual_leer.isnumeric() == False or int(cual_leer) > len(total) or int(cual_leer) == 0:
                print("No es un numero o es mayor que el numero de recetas")
                cual_leer = input(f"\nCUAL QUIERES LEER? ")
            else:
                pass
            # Elegimos un txt de la lista con el cual_leer
            fichero = total[int(cual_leer)-1]
            # Con el read_text() leemos el contenido del txt (se cierra tambien con ese metodo) y lo guardamos en data
            data = fichero.read_text()
            limpiar()
            # Imprimimos el contenido del txt
            print(data)


            # un simple codigo para volver al menu principal,quizas lo haga con una funcion
            if input("\n\n¿Quieres volver a la pantalla principal? [S/N]: ").lower() == "s":  # Si es S, volver al menu principal
                limpiar()
                os.execl(sys.executable, sys.executable, *sys.argv)
                continue
            else:
                limpiar()
                break

        if numero == "2":
            # vamos a mostrar las carpetas que hay
            limpiar()
            print(f"\n===SELECCIONA LA CATEGORÍA DESEADA=== \n")
            carpetas = sacar_carpetas_numeradas()

            seleccion1 = input("\nCATEGORÍA: ")
            if seleccion1 == "x":
                limpiar()
                os.execl(sys.executable, sys.executable, *sys.argv)
                pass
            else:
                pass
            seleccion1 = carpetas[int(seleccion1)-1]  # Ahora seleccion1 es el nombre de la carpeta que ha escogido el usuario
            # Ahora vamos a crear un archivo de texto con el nombre que el usuario quiera
            limpiar()
            print("ESTAS EN LA CATEGORÍA: ", seleccion1)
            nombre = input("\nNOMBRE DE LA RECETA: ")
            nombre = nombre + ".txt"
            # Creamos el archivo
            fichero = ruta2 / seleccion1 / nombre
            fichero.touch()
            # Ahora vamos a escribir en el archivo
            limpiar()
            print(f"\n===ESCRIBIENDO EN EL ARCHIVO {nombre}===")
            print(f"\n-Escribe lo que quieras y cuando quieras salir escribe x y pulsa enter.\n")
            # abrimos el txt para que el usuario pueda escribir en el y le preguntamos si quiere salir al menu principal
            with open(fichero, "w") as f:
                while True:
                    texto = input()
                    if texto == "x":
                        print("Guardando y saliendo...")
                        break
                    else:
                        f.write(texto + "\n")
            if input("\n\n¿Quieres volver a la pantalla principal? [S/N]: ").lower() == "s":  # Si es S, volver al menu principal
                limpiar()
                os.execl(sys.executable, sys.executable, *sys.argv)
                continue
            else:
                limpiar()
                break

        if numero == "3":
        # Vamos a crear una categoria nueva con el nombre que el usuario quiera
            limpiar()
            print(f"\n===CREANDO UNA NUEVA CATEGORÍA===")
            nombre = input("\nNOMBRE DE LA CATEGORÍA: ")
            # Creamos la carpeta
            while nombre == "x":
                print("No puedes crear una carpeta con ese nombre")
                nombre = input("\nNOMBRE DE LA CATEGORÍA: ")
            else:
                carpeta = ruta2 / nombre
                carpeta.mkdir()
                print(f"\n===CATEGORÍA {nombre} CREADA===")
            if input("\n\n¿Quieres volver a la pantalla principal? [S/N]: ").lower() == "s":  # Si es S, volver al menu principal
                limpiar()
                os.execl(sys.executable, sys.executable, *sys.argv)
                continue
            else:
                limpiar()
                break

        if numero == "4":
         # Vamos a eliminar el txt que el usuario quiera
            limpiar()
            print(f"\n===SELECCIONA LA CATEGORÍA DESEADA=== \n")
            carpetas = sacar_carpetas_numeradas()

            seleccion1 = input("\nCATEGORÍA: ")
            seleccion1 = carpetas[int(seleccion1)-1]  # Ahora seleccion1 es el nombre de la carpeta que ha escogido el usuario
         # vamos a mostar los txt que hay en la carpeta que el usuario ha escogido
            limpiar()
            print(f"\n===SELECCIONA LA RECETA QUE QUIERES ELIMINAR=== \n")
            total = []
            for fichero in ruta2.glob(f"{seleccion1}/*.txt"):
                total.append(fichero)
            # limpiamos los resultados de total
            for indice,valor in enumerate(total):
                total[indice] = valor.name
            # imprimir los resultados con numeros
            for indice,valor in enumerate(total,1):
                print(f"[{indice}]-[{valor}]")
            print(f"\n[x]-[Volver al menú principal]")
            cual_borrar = input("\nCUAL QUIERES BORRAR? ")
            while cual_borrar == "x":
                print("No puedes borrar esa receta")
                cual_borrar = input("\nCUAL QUIERES BORRAR? ")
            else:
                fichero = total[int(cual_borrar)-1]
                fichero = ruta2 / seleccion1 / fichero
                fichero.unlink()
                fichero_nombre = fichero.name

                print(f"\n===RECETA {fichero_nombre} ELIMINADA===")
            if input("\n\n¿Quieres volver a la pantalla principal? [S/N]: ").lower() == "s":  # Si es S, volver al menu principal
                limpiar()
                os.execl(sys.executable, sys.executable, *sys.argv)
                continue
            else:
                limpiar()
                break

        if numero == "5":
            # Vamos a eliminar la carpeta que el usuario quiera
            limpiar()
            print(f"\n===SELECCIONA LA CATEGORÍA QUE QUIERES ELIMINAR=== \n")
            carpetas = sacar_carpetas_numeradas()

            cual_borrar = input("\nCUAL QUIERES BORRAR? ") # Ahora cual_borrar es el numero de la carpeta que el usuario ha escogido pero que no supere el numero de carpetas que hay

            while cual_borrar != "x":
                if cual_borrar > str(len(carpetas)) or cual_borrar < "1":
                    print("No existe esa carpeta")
                    cual_borrar = input("\nCUAL QUIERES BORRAR? ")
                else:
                    # borramos la carpeta que el usuario ha escogido aunque no este vacia
                    cual_borrar = carpetas[int(cual_borrar)-1]
                    cual_borrar = ruta2 / cual_borrar
                    shutil.rmtree(cual_borrar,ignore_errors=True)
                    cual_borrar_nombre = cual_borrar.name
                    print(f"\n===CATEGORÍA {cual_borrar_nombre} ELIMINADA===")
                    break

            if input("\n\n¿Quieres volver a la pantalla principal? [S/N]: ").lower() == "s":
                limpiar()
                os.execl(sys.executable, sys.executable, *sys.argv)
                continue
            # otra opcion sin reiniciar el programa seria...
            # if input("\n\n¿Quieres volver a la pantalla principal? [S/N]: ").lower() == "s":  # Si es S, volver al menu principal
            #     limpiar()
            #     menu_principal()
            #     numero = input("\n\nSELECCIONA UNA OPCIÓN: ")
            #     continue
            else:
                limpiar()
                break





        else:  # Si es 6 break (Por ahora tambien estan los otros numeros)
            break




    else:
        numero = input("No es un numero o no esta entre el 1 y el 6: ")
        return principal(numero)



principal(numero)




