class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Linked:
    def __init__(self):
        self.head = None

    def addEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = newNode

    def printer(self):
        if self.head is None:
            print('This is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref


li = Linked()
li.addEnd(20)
li.addEnd(50)
li.addEnd(10)
li.printer()

