import networkx as nx
import matplotlib.pyplot as plt
from heap import FibonacciHeap
from node import Node

def drawHeap(heap):
    G = nx.Graph()
    node = heap.minRoot
    q = []
    while True:
        q.append(node)
        G.add_node(node.key, color="green" if node == heap.minRoot else "blue")
        G.add_edge(node.key, node.next.key)
        node = node.next
        if node == heap.minRoot:
            break
    while len(q) > 0:
        v = q.pop(0)
        child = v.minChild
        while child != None:
            q.append(child)
            G.add_node(child.key, color="red")
            G.add_edge(child.key, v.key)
            child = child.next
            if child == v.minChild:
                break
    colors = list(map(lambda x: x[1]['color'], G.nodes(data=True)))
    nx.draw(G, with_labels=True, node_color=colors)
    plt.show()

def insert():
    x5 = Node(5)
    x9 = Node(9)
    x7 = Node(7)
    x3 = Node(3)
    x4 = Node(4)
    x8 = Node(8)
    x10 = Node(10)

    x5.insertAfter(x7)
    x7.insertAfter(x3)

    x7.insertChild(x9)

    x8.insertChild(x10)
    x3.insertChild(x8)
    x8.insertAfter(x4)

    heap = FibonacciHeap(x3)
    print("before insert, minimum root key:",heap.minRoot.key)
    drawHeap(heap)

    heap.insert(2)

    print("after insert, minimum root key:",heap.minRoot.key)
    drawHeap(heap)

def union():
    x3 = Node(3)
    x8 = Node(8)
    x3.insertChild(x8)
    x11 = Node(11)
    x3.insertAfter(x11)
    x15 = Node(15)
    x11.insertChild(x15)
    x17 = Node(17)
    x11.insertChild(x17)
    x18 = Node(18)
    x15.insertChild(x18)
    h1 = FibonacciHeap(x3)
    print("heap 1 before union")
    drawHeap(h1)

    x7 = Node(7)
    x19 = Node(19)
    x7.insertAfter(x19)
    x20 = Node(20)
    x19.insertChild(x20)
    x28 = Node(28)
    x20.insertChild(x28)
    x25 = Node(25)
    x19.insertChild(x25)
    h2 = FibonacciHeap(x7)
    print("heap 2 before union")
    drawHeap(h2)

    print("heap after union")
    h1.merge(h2)
    drawHeap(h1)

def extract_min():
    x7 = Node(7)
    x9 = Node(9)
    x7.insertChild(x9)
    x2 = Node(2)
    x4 = Node(4)
    x2.insertChild(x4)
    x3 = Node(3)
    x2.insertChild(x3)
    x6 = Node(6)
    x4.insertChild(x6)
    x7.insertAfter(x2)

    print("heap before extract-min")
    h = FibonacciHeap(x7)
    drawHeap(h)

    print("heap after extract-min")
    h.extractMin()
    drawHeap(h)

def decrease_key():
    x7 = Node(7)
    x9 = Node(9)
    x7.insertChild(x9)
    x2 = Node(2)
    x4 = Node(4)
    x2.insertChild(x4)
    x3 = Node(3)
    x2.insertChild(x3)
    x6 = Node(6)
    x4.insertChild(x6)
    x7.insertAfter(x2)

    print("heap before decreasing key 9 to 1")
    h = FibonacciHeap(x7)
    drawHeap(h)

    h.decreaseKey(x9, 1)
    drawHeap(h)


def main():
    insert()
    union()
    extract_min()
    decrease_key()

main()