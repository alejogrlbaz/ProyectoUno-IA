
from collections import deque

def find_next(coordinates, maze):
    #Arreglo para almacenar las posiciones vecinas
    next_coordinates = []
    #Se verifica cuales posiciones se pueden transcurrir
    #Posición vecina de arriba
    if coordinates[0] - 1 >= 0 and maze[coordinates[0] - 1][coordinates[1]] != 1:
        next_coordinates.append((coordinates[0] - 1, coordinates[1]))
    #Posicion vecina de abajo
    if coordinates[0] + 1 < len(maze) and maze[coordinates[0] + 1][coordinates[1]] != 1:
        next_coordinates.append((coordinates[0] + 1, coordinates[1]))
    #Posicion vecina de la derecha
    if coordinates[1] + 1 < len(maze[0]) and maze[coordinates[0]][coordinates[1] + 1] != 1:
        next_coordinates.append((coordinates[0], coordinates[1] + 1))
    #Posicion vecina de la izquierda
    if coordinates[1] - 1 >= 0 and maze[coordinates[0]][coordinates[1]  - 1] != 1:
        next_coordinates.append((coordinates[0], coordinates[1] - 1))
    return next_coordinates

def bfs(maze, start, goals):
    queue = deque()
    way = []
    visited = set()
    cont_goals = 0
    goal_one = goals[0]
    goal_two = goals[1]
    queue.append(start)
    while queue:
        print("\n")
        n = queue.popleft()
        print(f"Popping {n}"+'='+str(maze[n[0]][n[1]]))
        way.append(n)
        print(f"Is {n} my goal?")
        if (n == goal_one) or (n == goal_two):
            print("DONE!")
            cont_goals = cont_goals+1
        if cont_goals == 2:
            print(f"Way: {way}")
            return way
        print(f"No.")
        next_steps = find_next(n, maze)
        print(f"Next Steps: {next_steps}")
        for x in next_steps:
            print(f"Evaluating {x}")
            if x in visited:
                print(f"{x} already visited, skipping...")
                continue
            visited.add(x)
            queue.append(x)
            print(f"Visited nodes: {visited}")
            print(f"Queue: {queue}")
