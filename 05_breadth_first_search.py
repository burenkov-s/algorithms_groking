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
            print(vertex)
#            search_queue += list(vertex.adjacent)

            searched.append(Vertex)


