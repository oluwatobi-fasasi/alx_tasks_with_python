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
link1.print_element()
