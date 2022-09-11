class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None



class Linked:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node


    def add_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = newNode


    def print_element(self):
        if self.head is None:
            print('This Linked list is empty')

        else:
            n = self.head
            l = []
            while n is not None:
                l.append(n.data)
                n = n.ref
            print(l, len(l))

link1 = Linked()
for i in range(50, 9, -10):
    link1.add_begin(i)
    link1.add_end(i*2)
link1.print_element()
