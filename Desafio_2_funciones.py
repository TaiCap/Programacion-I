#Funcion para cargar los datos de todos los jugadores

def datos_jugadores(jugadores:int):
    matriz = [["" for i in range(5)]for j in range(jugadores)]      

    for a in range(jugadores):                                                  
        matriz[a][0] = input(f"Ingrese el nombre del jugador {a+1}: ")          
        matriz[a][1] = input(f"Ingrese el apellido del jugador {a+1}: ")        
        matriz[a][2] = input(f"Ingrese la edad del jugador {a+1}: ")            
        matriz[a][3] = input(f"Ingrese el posicion del jugador {a+1}: ")
        matriz[a][4] = input(f"Ingrese la cantidad de goles que realizo el jugador {a+1}: ")

    return matriz


#Funcion para mostrar los datos de todos los jugadores

def mostrar_datos(matriz:list, jugadores:int):      
    print("")
    print("///Datos Jugadores///")
    print("")

    for f in range(jugadores):                     
        print(f"Jugador {f + 1}")                 
        print(f"Nombre: {matriz[f][0]}")           
        print(f"Apellido: {matriz[f][1]}")
        print(f"Edad: {matriz[f][2]} años")
        print(f"Posición: {matriz[f][3]}")
        print(f"Goles: {matriz[f][4]}")
        print("")

#Funcion para modificar los datos de todos los jugadores

def modificar_datos(matriz:list):
    jugador_fila = int(input("Ingresa el numero del jugador que vas a modificar: "))
    estadistica_columna = int(input("¿Que dato queres modificar?\n[1] Nombre\n[2] Apellido\n[3] Edad\n[4] Posicion\n[5] Goles\n"))
    nuevo_dato = input("Ingrese el cambio: ")

    matriz[jugador_fila - 1][estadistica_columna - 1] = nuevo_dato   
    
    return matriz
       