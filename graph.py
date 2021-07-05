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

    def add_vertex(self, new_vertex):
        for vertex in self.vertices:
            if str(vertex) == str(new_vertex):
                print ("Such vertex already exists.")
                return None
        if new_vertex is Vertex:
            self.vertices.add(new_vertex)
        else:
            self.vertices.add(Vertex(new_vertex))

    def add_edge(self, vertex1, vertex2):
        vertex1.add_adjacent(vertex2.name)
        vertex2.add_adjacent(vertex1.name)

    def get_adjacent(self, needed_vertex):
        for vertex in self.vertices:
            if (str(vertex) == needed_vertex):
                return vertex.get_adjacent()

if __name__ == "__main__":
#    A = Vertex('A')
#    B = Vertex('B')
#    C = Vertex('C')
    #A.add_adjacent('B')
    #A.add_adjacent('C')
    # B.add_adjacent('A')
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex("B")
    graph.add_vertex('C')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')

    for vertex in graph:
        print(vertex)
        print(type(vertex))
    print(graph.get_adjacent(A))
    print(A.get_adjacent())

#    print(graph.get_adjacent('B'))

#    print(A.get_adjacent())
