import networkx as nx
import matplotlib.pyplot as plt
from heap import HollowHeap, Node, Item

def drawHeap(heap):
    G = nx.DiGraph(directed=True)
    node = heap.h
    q = []
    q.append(node)
    G.add_node(node.key, color="green")
    while len(q) > 0:
        v = q.pop(0)
        child = v.child
        while child != None: # and child not in seen:
            q.append(child)
            color = "blue" if child.child == None else "red"
            color = color if child.item != None else "purple"
            G.add_node(child.key, color=color)
            G.add_edge(child.key, v.key, style="dotted" if child.ep == v else "solid")
            if child.ep == v:
                break
            child = child.next
    colors = list(map(lambda x: x[1]['color'], G.nodes(data=True)))
    styles = list(map(lambda x: x[2]['style'], G.edges(data=True)))
    nx.draw(G, node_color=colors, with_labels=True, arrows=True, style=styles)
    plt.show()

def insert(heap):
    # 14, 11, 5, 9, 0, 8, 10, 3, 6, 12, 13, 4
    heap.insert(Item(), 14)
    heap.insert(Item(), 11)
    item5 = Item()
    heap.insert(item5, 5)
    heap.insert(Item(), 9)
    heap.insert(Item(), 0)
    item8 = Item()
    heap.insert(item8, 8)
    heap.insert(Item(), 10)
    item3 = Item()
    heap.insert(item3, 3)
    heap.insert(Item(), 6)
    heap.insert(Item(), 12)
    heap.insert(Item(), 13)
    heap.insert(Item(), 4)
    drawHeap(heap)
    return (item5, item3, item8)

def delete_min(heap):
    heap.delete_min()
    drawHeap(heap)

def decrease_key(heap, items):
    heap.decrease_key(items[0], 1)
    heap.decrease_key(items[1], 2)
    heap.decrease_key(items[2], 7)
    drawHeap(heap)

def main():
    heap = HollowHeap()

    print("inserting 14, 11, 5, 9, 0, 8, 10, 3, 6, 12, 13, 4 into hollow heap")
    items = insert(heap)

    print("deleting minimum")
    delete_min(heap)

    print("decrease key 5 to 1, then key 3 to 2 and then key 8 to 7")
    decrease_key(heap, items)

    print("second delete minimum")
    delete_min(heap)

    print("third delete minimum")
    delete_min(heap)

main()