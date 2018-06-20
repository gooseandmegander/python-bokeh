class Edge:
    def __init__(self, destinaton):
        self.destinaton = destinaton

class Vertex:
    def __init__(self, value, **pos):
        self.value = value
        self.pos = pos
        self.color = 'color'
        self.edges = []

class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x=40, y=40)
        debug_vertex_2 = Vertex('t2', x=140, y=140)

        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)

        self.vertexes.append(debug_vertex_1)
        self.vertexes.append(debug_vertex_2)