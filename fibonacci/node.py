class Node:
    def __init__(self, 
        key,
        prev = None, 
        next = None, 
        parent = None, 
        minChild = None, 
        degree = 0, 
        marked = False):

        self.prev = prev if prev != None else self
        self.next = next if next != None else self
        self.parent = parent
        self.minChild = minChild
        self.key = key
        self.degree = degree
        self.marked = marked

    def insertAfter(self, newNode):
        newNode.next = self.next
        newNode.prev = self
        self.next.prev = newNode
        self.next = newNode
        newNode.parent = self.parent
        if self.parent != None:
            self.parent.degree += 1

    def insertChild(self, newChild):
        if self.key < newChild.key:
            if self.minChild == None:
                newChild.prev = newChild
                newChild.next = newChild
                self.minChild = newChild
                newChild.parent = self
                self.degree += 1
            else:
                self.minChild.insertAfter(newChild)
        else newChild.insertChild(self)
            