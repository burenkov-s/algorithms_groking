class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacent = set()

    def __str__(self):
            return str(self.name)

    def get_adjacent(self):
        return list(self.adjacent)



    def add_adjacent(self, neighbor):
        self.adjacent.add (neighbor)

class Graph:
    def __init__(self):
        self.vertices = set()

    def __iter__(self):
        return iter(self.vertices)

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, vertex1, vertex2):
        vertex1.add_adjacent(vertex2.name)
        vertex2.add_adjacent(vertex1.name)

    def get_adjacent(self, needed_vertex):
        for vertex in self:
            if vertex == needed_vertex:
                vertex.get_adjacent()

if __name__ == "__main__":
    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    #A.add_adjacent('B')
    #A.add_adjacent('C')
    # B.add_adjacent('A')
    graph = Graph()
    graph.add_vertex(A)
    graph.add_vertex(B)
    graph.add_vertex(C)
    graph.add_edge(A, B)
    graph.add_edge(A, C)
    for vertex in graph:
        print(vertex)
    print(graph.get_adjacent('A'))
