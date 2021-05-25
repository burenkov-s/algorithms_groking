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

    def find(self,data):
        # finds first occurence of the element
        elem_pos = 0
        for elem in self:
            if elem.data == data:
                print("Element", elem.data, "at position", elem_pos)
                return
            elem_pos += 1
        print("Element not found")

    def print(self):
        #prints elements separated by "->"
        print("List:")
        for elem in self:
            if elem.next is not None:
                print(elem.data, "-> ", end='')
            else:
                print(elem.data)

    def remove(self, data):
        #removes first found element
        if self.head == None:
            print("List is empty")
            return

        if self.head.data == data:
            self.head = self.head.next

        prev_node = self.head
        for node in self:
            if node.data == data:
                prev_node.next = node.next
                return
            prev_node = node

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

llist = LinkedList()
#add elements for testing
llist.add('a')
llist.add('b')
llist.add('c')
#print(llist.head.next.data)
while True:
    print ( "1.add element to list\n"
            "2.print list\n"
            "3.find element in list\n"
            "4.remove element\n"
            "0.exit\n" )
    menu = input()
    if menu == '1':
        print("Enter element:")
        llist.add(input())
    if menu == '2':
        llist.print()
    if menu == '3':
        print("Enter element:")
        llist.find(input())
    if menu == '4':
        print("Enter element:")
        llist.remove(input())
    if menu == '0':
        break
