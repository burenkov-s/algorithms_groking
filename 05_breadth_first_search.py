from collections import deque
from graph import Graph, Vertex

class Graph(Graph):
    def search(self, starting_vertex, needed_vertex):
        search_queue = deque()
        search_queue += self.vertex(starting_vertex).get_adjacent()
        searched = []
        while search_queue:
            vertex = search_queue.popleft()
            if vertex not in searched:
                if needed_vertex == vertex:
                    print("There is a path between vertices")
                    return self.vertex(needed_vertex)
                else:
                    search_queue += self.vertex(vertex).get_adjacent()
                    searched.append(vertex)
        print("There is no path between vertices")

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A','B')
graph.add_edge('B','C')
graph.add_edge('B','D')

while True:
    print ( "1.add element to graph\n"
            "2.add edge between elements\n"
            "3.find path between two vertices\n"
            "4.print graph\n"
            "0.exit\n" , end='')

    menu = input()

    if menu == "1":
        graph.add_vertex(input("Enter name of vertex to add: \n"))

    if menu == "2":
        graph.add_edge(input("Enter name of first vertex: \n"),
            input("Enter name of second vertex: \n"))

    if menu == "3":
        graph.search(input("Enter name of starting vertex: \n"),
            input("Enter name of needed vertex: \n"))
#        graph.search("A", "C")
    if menu == "4":
        for vertex in graph:
            print(vertex)

    if menu == "0":
        print("Exiting.")
        break
"""
search_queue = deque()
search_queue += list(A.adjacent) # starting from A
searched = []


needed_vertex = input("Enter name of needed vertex: \n")

while search_queue:
    vertex = search_queue.popleft()
    if vertex not in searched:
        if vertex == needed_vertex:
            print("Vertex found")
        else:
           search_queue += list(graph.get_adjacent(vertex))
           searched.append(vertex)
"""
