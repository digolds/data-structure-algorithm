class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, cost, adjacent_vertex_index):
        self.cost = cost
        self.adjacent_vertex_index = adjacent_vertex_index

class Graph:
    def __init__(self):
        self.vertexes = []
        self.edges = []
    
    def add_vertex(self, value):
        pass
    
    def remove_vertex(self):
        pass
