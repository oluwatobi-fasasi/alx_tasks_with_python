class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Linked:
    def __init__(self):
        self.head = None

    def addBegin(self, data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head = newNode

    def addEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = newNode

    def addAfterNode(self, data, x):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.ref
            newNode.ref = n.ref
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
for i in range(50, 9, -10):
    li.addBegin(i)
    li.addEnd(i/2)
li.addAfterNode(500, 20)
li.printer()
