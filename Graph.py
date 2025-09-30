from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edges(self,u,v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u)
    def show_graph(self):
        for vertex in self.graph:
            print(vertex,"->",self.graph[vertex])
    
    def BFS(self,start):
        if start not in self.graph:
            return 0
        visted =set()
        visted.add(start)
        q =deque([start])
        while q:
            vertex =q.popleft() 
            print("visted-",vertex,end="")
            for neighbour in self.graph[vertex]:
                if neighbour not in visted:
                    visted.add(neighbour)
                    q.append(neighbour)    
        #print(visted)
    
    def DFS(self,start,visted=None):
        if visted is None:
            visted =set()
        visted.add(start)
        print("visted",start)
        for neighbour in self.graph[start]:
            if neighbour not in visted:
                self.DFS(neighbour,visted)
    
    def count(self):
        edge_list=[]
        for i in self.graph:
            for j in self.graph[i]:
                edge_list.append(j)
        edges =len(edge_list)//2
        vertex =len(self.graph)
        print("Vertex-",vertex,"Edges-",edges)
    
    def degree_vertex(self,vertex):
        if vertex in self.graph:
            print(len(self.graph[vertex]))
        else:
            return 0
            
g =Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(5)
g.add_vertex(4)

g.add_edges(1,2)
g.add_edges(1,3)
g.add_edges(2,4)
g.add_edges(2,5)
g.add_edges(3,5)

#g.show_graph()
#g.BFS(1)
#g.DFS(1)
#g.count()
#g.degree_vertex(2)