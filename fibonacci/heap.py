from node import Node
import sys
import math

class FibonacciHeap:
    def __init__(self, node: Node = None):
        self.minRoot = self.min(node)
        self.n = 0 if node == None else 1

    def min(self, node: Node):
        if node == None:
            return None
        best = node
        curr = node.next
        while curr != node:
            if curr.key < best.key:
                best = curr
            curr = curr.next
        return best

    def updateMin(self, candidate):
        if candidate != None:
            if self.minRoot == None or self.minRoot.key > candidate.key:
                self.minRoot = candidate

    def removeNode(self, node: Node):
        if node == self.minRoot:
            self.minRoot = node.next
        node.prev.next = node.next
        node.next.prev = node.prev

    def findMin(self):
        return self.minRoot

    def merge(self, other):
        otherRoot = other.findMin()
        if self.minRoot == None:
            self.minRoot = otherRoot
        elif otherRoot == None:
            return
        else:
            # whats wrong here
            self.minRoot.next.prev = otherRoot.prev
            otherRoot.prev.next = self.minRoot.next
            self.minRoot.next = otherRoot
            otherRoot.prev = self.minRoot
            self.updateMin(otherRoot)
        self.n += other.n

    def insert(self, key):
        node = Node(key)
        newHeap = FibonacciHeap(node)
        self.merge(newHeap)

    def extractMin(self):
        z = self.minRoot
        if z != None:
            node = z.minChild
            # Update children of minRoot to be roots (no parents)
            children = []
            while node != None:
                #node.parent = None
                children.append(node)
                node = node.next
                if node == z.minChild:
                    break

            for n in children:
                self.minRoot.insertAfter(n)
            # Add children of minRoot to root list
            #self.merge(FibonacciHeap(node))

            # Remove minRoot from root list
            self.removeNode(z)

            if z == z.next:
                # minRoot was only root in root list with no children
                self.minRoot = None
            else:
                self.minRoot = z.next
                self.n -= 1
                self.consolidate()
            self.n -= 1

    def consolidate(self):
        A = []
        D = 255
        for i in range(D):
            A.append(None)
        r = self.minRoot
        nodes = []
        while True:
            nodes.append(r)
            r = r.next
            if r == self.minRoot:
                break
        for w in nodes:
            x = w
            d = x.degree
            while A[d] != None:
                y = A[d]
                if x.key > y.key:
                    # exchange x and y
                    z = x
                    x = y
                    y = z
                self.link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        self.minRoot = None
        for i in range(D):
            if A[i] != None:
                if self.minRoot == None:
                    self.minRoot = A[i]
                    self.minRoot.next = self.minRoot
                    self.minRoot.prev = self.minRoot
                else:
                    self.minRoot.insertAfter(A[i])
                    if self.minRoot.key > self.minRoot.next.key:
                        self.minRoot = A[i]

    def link(self, y: Node, x: Node):
        self.removeNode(y)
        y.parent = x
        if x.minChild != None:
            x.minChild.insertAfter(y)
        else:
            x.minChild = y
            y.next = y
            y.prev = y
        x.degree += 1
        y.marked = False

    def decreaseKey(self, node: Node, key: int):
        if key > node.key:
            raise Exception("New key is greater than the value of the old key")
        node.key = key
        y = node.parent
        if y != None and y.key > node.key:
            self.cut(node, y)
            self.cascading_cut(y)
        self.updateMin(node)

    def cut(self, x: Node, y: Node):
        if y.degree < 2:
            y.minChild = None
        else:
            if y.minChild == x:
                y.minChild = x.next
                x.next.parent = y
            self.removeNode(x)
        y.degree -= 1
        self.minRoot.insertAfter(x)
        x.parent = None
        x.marked = False

    def cascading_cut(self, node: Node):
        z = node.parent
        if z != None:
            if node.marked == False:
                node.marked = True
            else:
                self.cut(node, z)
                self.cascading_cut(z)

    def delete(self, node: Node):
        self.decreaseKey(node, -sys.maxsize)
        self.extractMin()