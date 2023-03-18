"""Breadth First Traversal for a Graph"""

from collections import defaultdict 

class Graph: 

    def __init__(self): 

        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to the graph 
    def add_edge(self,u,v): 
        self.graph[u].append(v) 

    # function to perform Breadth First Traversal of the graph 
    def bfs(self, start_vertex): 

        # initialize a queue for BFS 
        queue = [] 

        # mark the start_vertex as visited and enqueue it 
        visited = [False] * (max(self.graph)+1) 
        queue.append(start_vertex) 
        visited[start_vertex] = True

        while queue: 

            # dequeue a vertex from the queue and print it 
            start_vertex = queue.pop(0) 
            print(start_vertex, end = " ") 

            # get all adjacent vertices of the dequeued vertex s 
            # if an adjacent has not been visited, mark it as visited 
            # and enqueue it 
            for i in self.graph[start_vertex]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True

# creating a graph object 
g = Graph() 

# asking user for the number of vertices and edges
V = int(input("Enter the number of vertices: ")) 
E = int(input("Enter the number of edges: ")) 

# asking user to enter the edges of the graph 
for i in range(E): 
    u,v = map(int,input("Enter the edge (u, v): ").split()) 
    g.add_edge(u, v) 

# asking user for the starting vertex
start_vertex = int(input("Enter the starting vertex: "))

print("Breadth First Traversal (starting from vertex", start_vertex, "):") 
g.bfs(start_vertex) 
