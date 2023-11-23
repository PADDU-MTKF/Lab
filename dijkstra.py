def dijkstra(graph, start): 
    numvertices = len(graph) 
    distances = [float('inf')] * numvertices 
    penultimate_vertices = [None] * numvertices 
    visited = [False] * numvertices 
    distances[start] = 0 
    for _ in range(numvertices): 
        min_distance = float('inf') 
        min_vertex = -1 
        # Find the vertex with the smallest distance that has not been visited 
        for v in range(numvertices): 
            if not visited[v] and distances[v] < min_distance: 
                min_distance = distances[v] 
                min_vertex = v 
                
        if min_vertex == -1: 
            break 
        
        visited[min_vertex] = True 
        for v in range(numvertices): 
            if not visited[v] and graph[min_vertex][v] > 0: 
                newdistance = distances[min_vertex] + graph[min_vertex][v] 
                if newdistance < distances[v]: 
                    distances[v] = newdistance 
                    penultimate_vertices[v] = min_vertex 
    return distances, penultimate_vertices 



def get_path(penultimate_vertices, destination): 
    path = [destination] 
    while penultimate_vertices[destination] is not None: 
        destination = penultimate_vertices[destination] 
        path.insert(0, destination) 
    return path 


no_vertices = int(input("Enter the number of vertices: ")) 
graph = [] 
print(f'Enter the weight adjacency Matrix:') 

for i in range(no_vertices): 
    row = list(map(int, input(f'Enter weight of the vertex {i} : ').split())) 
    graph.append(row) 

start_vertex = int(input(f"Enter the start vertex (0 to {no_vertices-1}) :")) 
distances, penultimate_vertices = dijkstra(graph, start_vertex) 

for vertex, distance in enumerate(distances): 
    if vertex != start_vertex: 
        path_to_vertex = get_path(penultimate_vertices, vertex) 
        print(f"Shortest distance from {start_vertex} to {vertex} is {distance}, path: {path_to_vertex}") 