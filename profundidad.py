import pygame
import pygame_gui
import startPage


 
way_global=[]


#Esta función me identifica las posiciones vecinas y si me puedo mover a ellas
def find_next(position, matriz):
    #Arreglo para almacenar las posiciones vecinas
    next_positions = []
    #Se verifica cuales posiciones se pueden transcurrir
    #Posición vecina de arriba
    if position[0] - 1 >= 0 and matriz[position[0] - 1][position[1]] != 1:
        next_positions.append((position[0] - 1, position[1]))
    #Posicion vecina de abajo
    if position[0] + 1 < len(matriz) and matriz[position[0] + 1][position[1]] != 1:
        next_positions.append((position[0] + 1, position[1]))
    #Posicion vecina de la derecha
    if position[1] + 1 < len(matriz[0]) and matriz[position[0]][position[1] + 1] != 1:
        next_positions.append((position[0], position[1] + 1))
    #Posicion vecina de la izquierda
    if position[1] - 1 >= 0 and matriz[position[0]][position[1]  - 1] != 1:
        next_positions.append((position[0], position[1] - 1))
    return next_positions


#Esta función realiza el proceso de encontrar la meta y recorrer los nodos
def dfs(matriz, start, goals):
    print("longitud de matriz"+str(len(matriz)))
    stack = []
    way =[]
    visited = set()
    cont_goals=0
    goal_one = goals[0]
    goal_two = goals[1]
    stack.append(start)
    while stack:
        print("\n")
        n = stack.pop()
        #print(f"Popping {n}"+'='+str(matriz[n[0]][n[1]]))
        #Se escoge el ultimo que esté en el stack
        way.append(n)
        print(f"Is {n} my goal?")
        #Verificamos si nos encontramos en alguna de las metas
        if (n == goal_one) or (n == goal_two):
            print("DONE!")
            #Aumentamos el contador de metas, esto se hace para verificar cuantas metas ha encontrado
            cont_goals = cont_goals+1
        if cont_goals == 2:
            #Si ya se encontraron las dos metas entonces imprimimos el camino y lo retornamos
            print(f"Way: {way}")
            return way
        print(f"No.")
        #Si no se ha encontrado las dos metas continuamos buscando
        #Llamamos la funcion find_next para evaluar el proximo paso
        next_steps = find_next(n, matriz)
        print(f"Next Steps: {next_steps}")
        #Evaluamos los posibles pasos
        for x in next_steps:
            print(f"Evaluating {x}")
            #Evaluamos si ya lo hemos visitado antes
            if x in visited:
                print(f"{x} already visited, skipping...")
                continue
            #Si no lo hemos visitado entonces ya lo agregamos a visitado
            visited.add(x)
            #lo mandamos como 
            stack.append(x)
            print(f"Visited nodes: {visited}")
            print(f"Stack: {stack}")