class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data = element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return nodes

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add(self, data):
        if self.head:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        else:
            self.head = Node(data)

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
"""
first_node = Node("a")
second_node = Node("b")
third_node = Node("c")

llist.head = first_node
first_node.next = second_node
second_node.next = third_node
"""
llist = LinkedList()
llist.add("d")
llist.add("c")
#print (repr(llist))
#print(llist)
#repr(llist)
for element in llist:
    print (element)
