"""Depth First Traversal for a Graph"""

from collections import defaultdict 

class Graph: 

    def __init__(self): 

        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to the graph 
    def add_edge(self,u,v): 
        self.graph[u].append(v) 

    # function to perform Depth First Traversal of the graph 
    def dfs(self, start_vertex, visited): 

        # mark the start_vertex as visited 
        visited.add(start_vertex) 
        print(start_vertex, end=' ')

        # recursively traverse all the adjacent vertices of the start_vertex
        for next_vertex in self.graph[start_vertex]: 
            if next_vertex not in visited: 
                self.dfs(next_vertex, visited) 

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

print("Depth First Traversal (starting from vertex", start_vertex, "):") 
visited = set() 
g.dfs(start_vertex, visited) 
