puntuaciones = []

def puntuacion():
    # Ingreso de puntuación y comentario
    while True:
        print("Por favor, introduzca una puntuación en una escala de 1 a 5")
        valor = input()
        
        if valor.isdecimal():
            valor = int(valor)
            if valor >= 1 and valor <= 5:
                break
            else:
                print("Por favor, introduzca una puntuación válida en la escala de 1 a 5")
        else:
            print("Por favor, introduzca la puntuacion en números enteros")
    
    print("Por favor, deje su comentario")
    comentario = input()
    
    # Guardamos en la lista
    puntuaciones.append((valor, comentario))
    # Escribimos en el archivo
    with open("datos.txt", 'a') as file_pc:
        file_pc.write(f'Puntuacion: {valor}, Comentario: {comentario}\n')
    print("Puntuación y comentario guardados correctamente.")

def resultado():
    # Lectura y visualización de resultados
    print("Resultados hasta la fecha:")
    with open("datos.txt", "r") as read_file:
        print(read_file.read())

def finalizar():
    print("Finalizado")
    exit()  # Sale del programa

while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')
    
    num = input()
    if num == '1':
        puntuacion()
    elif num == '2':
        resultado()
    elif num == '3':
        finalizar()
    else:
        print("Introduzca un número del 1 al 3.")
