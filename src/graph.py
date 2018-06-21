import random

class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value, **pos):
        self.value = value
        self.pos = pos
        self.color = 'white'
        self.edges = []

class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x=40, y=40)
        debug_vertex_2 = Vertex('t2', x=140, y=140)
        debug_vertex_3 = Vertex('t3', x=300, y=500)
        debug_vertex_4 = Vertex('t4', x=500, y=300) # will remain unconnected

        debug_edge_start_a = Edge(debug_vertex_1)
        debug_edge_start_b = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_start_b)
        debug_vertex_2.edges.append(debug_edge_start_a)

        debug_edge_start_c = Edge(debug_vertex_3)
        debug_edge_start_d = Edge(debug_vertex_2)
        debug_vertex_2.edges.append(debug_edge_start_c)
        debug_vertex_3.edges.append(debug_edge_start_d)

        debug_edge_start_e = Edge(debug_vertex_1)
        debug_edge_start_f = Edge(debug_vertex_4)
        debug_vertex_4.edges.append(debug_edge_start_e)
        debug_vertex_1.edges.append(debug_edge_start_f)

        self.vertexes.extend([debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4])
    
    def bfs(self, start):
        random_color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

        queue = []
        found = []

        queue.append(start)
        found.append(start)

        start.color = random_color

        while len(queue) > 0:
            vertex = queue[0]
            for edge in vertex.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
            queue.pop(0) # TODO: Look into collections.dequeue
        return found 

