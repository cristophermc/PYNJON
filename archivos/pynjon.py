##Espacio de importación de módulos y otros enlaces referencias de archivos.py





##Espacio para definición de funciones importantes y rutinas:





##Programa principal:
if __name__=='__main__':
        while True:
            print('------------------------------------------')
            print('| \t\t \033[31mPYNJON\033[0m \t\t |')
            print("------------------------------------------")
            print("\t      MENU PRINCIPAL   \t")
            print("------------------------------------------")
            print("1. Lanzamiento de dados\n2. Tracker de iniciativa\n3. Tomar notas\n4. Generadores\n5. Consultar referencias del manual\n6. Salir de la aplicación")
            print('------------------------------------------')
            try:
                seleccion=int(input("SELECCIONA UN Nº >>> "))
            except ValueError:
                 print("Debes introducir un número para continuar con la aplicación.")
                 input("Pulse ENTER para continuar")
                 continue
            else:
                 match seleccion:
                      case 1:
                          #Se hace la llamada a la función de lanzar dados 
                          print("En construcción de la función")
                          pass
                      case 2:
                           #Se hace la llamada a la función de tracker de iniciativa 
                          print("En construcción de la función")
                      case 3:
                           #Se hace la llamada a la función de tomar notas 
                          print("En construcción de la función")
                      case 4:
                           #Se hace la llamada a la función de generadores 
                          print("En construcción de la función")
                      case 5:
                           #Se hace la llamada a la función de consultar referencias del manual 
                          print("En construcción de la función")
                      case 6:
                           print("Saliendo de la aplicación...")
                           exit() #función del sistema para salir de la aplicación