class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacent = set()

    def __str__(self):
        return str(self.name)

    def get_adjacent(self):
        return list(self.adjacent)

    def add_adjacent(self, neighbor):
        self.adjacent.add(neighbor)

class Graph:
    def __init__(self):
        self.vertices = set()

    def __iter__(self):
        return iter(self.vertices)

    def vertex(self, target_vertex):
        for vertex in self.vertices:
            if str(vertex) == str(target_vertex):
                return vertex

    def add_vertex(self, new_vertex):
        if self.vertex(new_vertex):
            print ("Such vertex already exists.")
            return None
        if new_vertex is Vertex:
            self.vertices.add(new_vertex)
        else:
            self.vertices.add(Vertex(new_vertex))

    def add_edge(self, vertex1, vertex2):
        self.vertex(vertex1).add_adjacent(vertex2)
        self.vertex(vertex2).add_adjacent(vertex1)


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_edge('A', 'B')
    print(graph.vertex('A').get_adjacent())
