import Desafio_2_funciones


cantidad_jugadores = 11
estado_menu = 1
estado_menu_2 = 1
estado_programa = 0
estado_programa_2 = 0
modificar_jugadores = 0


print("")
print("Bienvenido al gestor de equipos del torneo\nDebera ingresar [Nombre] [Apellido] [Edad] [Poisicion] [Cantidad de goles]\nSe tendran en cuenta solo los 11 jugadores del torneo")
print("")


while estado_menu == 1:
    estado_programa = int(input("Ingrese [1] para comenzar\n"))

    if estado_programa == 1:
        estado_menu = 0
        matriz_jugadores = Desafio_2_funciones.datos_jugadores(cantidad_jugadores)      
        Desafio_2_funciones.mostrar_datos(matriz_jugadores,cantidad_jugadores)
    else:
        print("Opcion no valida, intente nuevamente")



while estado_menu_2 == 1:
    estado_programa_2 = int(input("Ingrese [3] para modificar datos de los jugadores\nIngrese [4] para mostrar la lista actual\nIngrese [2] para salir\n"))

    if estado_programa_2 == 3:
        matriz_jugadores = Desafio_2_funciones.modificar_datos(matriz_jugadores)
    elif estado_programa_2 == 4:
        Desafio_2_funciones.mostrar_datos(matriz_jugadores,cantidad_jugadores)    
    elif estado_programa_2 == 2:
        estado_menu_2 = 0
        print("Apagando el programa...")
    else:
        print("Opcion no valida, intente nuevamente")
