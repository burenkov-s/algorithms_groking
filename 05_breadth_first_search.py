from collections import deque
from graph import Graph, Vertex

A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')

graph = Graph()
graph.add_vertex(A)
graph.add_vertex(B)
graph.add_vertex(C)
graph.add_vertex(D)
graph.add_edge(A,B)
graph.add_edge(B,C)
graph.add_edge(B,D)

while True:
    print ( "1.add element to graph\n"
            "2.add edge between elements\n"
            "3.find element in graph\n"
            "4.print graph\n"
            "0.exit\n" , end='')
    menu = input()
    if menu == "1":
        print("Enter name of vertex to add:")
        graph.add_vertex(Vertex(input()))
        for vertex in graph:
            print (vertex)
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
