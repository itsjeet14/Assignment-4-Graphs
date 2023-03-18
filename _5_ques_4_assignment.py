"""Detect Cycle in a Directed Graph"""

from collections import defaultdict 

class Graph: 
    def __init__(self, vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices
  
    def add_edge(self, u, v): 
        self.graph[u].append(v) 
  
    def is_cyclic_util(self, v, visited, rec_stack): 

        visited[v] = True
        rec_stack[v] = True
  
        for neighbour in self.graph[v]: 
            if not visited[neighbour]: 
                if self.is_cyclic_util(neighbour, visited, rec_stack): 
                    return True
            elif rec_stack[neighbour]: 
                return True
  
        rec_stack[v] = False
        return False
  
    def is_cyclic(self): 
        visited = [False] * self.V 
        rec_stack = [False] * self.V 
        for node in range(self.V): 
            if not visited[node]: 
                if self.is_cyclic_util(node,visited,rec_stack) == True: 
                    return True
        return False

# take user input for number of vertices and edges
V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))

# create a directed graph object
g = Graph(V)

# take user input for edges
print("Enter the edges in the format 'u v': ")
for i in range(E):
    u, v = map(int, input().split())
    g.add_edge(u, v)

if g.is_cyclic(): 
    print("The graph contains a cycle") 
else: 
    print("The graph does not contain a cycle") 
