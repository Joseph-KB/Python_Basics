'''
    Non linear DS 
    Nodes(vertices) and Edges(lines/arcs)
    Most used representations of graph
'''

class Graph:
    def __init__(self,numvertex) -> None:
        self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
        self.numvertex=numvertex
        self.vertices={}
        self.verticeslist=[0]*numvertex

    def set_vertex(self,vtx:str,id:int):
        if 0<=vtx<=self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id
            
    def set_edge(self,frm,to,cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost

    def get_vertex(self):
        return self.verticeslist
    
    def get_edges(self):
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if (self.adjMatrix[i][j] != -1):
                    edges.append((self.verticeslist[i],
                                  self.verticeslist[j],
                                  self.adjMatrix[i][j]))
        return edges
        
    def get_matrix(self):
        return self.adjMatrix
    
graph = Graph(6)
graph.set_vertex(0,'a')
graph.set_vertex(1,'b')
graph.set_vertex(2,'c')
graph.set_vertex(3,'d')
graph.set_vertex(4,'e')
graph.set_vertex(5,'f')
graph.set_edge('a','c',10)
graph.set_edge('a','e',20)
graph.set_edge('e','d',30)
graph.set_edge('d','f',40)
graph.set_edge('e','f',50)
graph.set_edge('c','d',60)

print("vertices of graph\n",graph.get_vertex())
print("Edges of graph\n",graph.get_edges())
print("Adjacency Matrix of graph\n",[print(x) for x in graph.get_matrix()])