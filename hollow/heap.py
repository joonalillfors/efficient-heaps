class Node:
    def __init__(self, e, k):
        self.item = e
        e.node = self
        self.child = None
        self.next = None
        self.ep = None
        self.key = k
        self.rank = 0

    def add_child(self, v):
        v.next = self.child
        self.child = v

    def link(self, v):
        if self.key >= v.key:
            v.add_child(self)
            return v
        else:
            self.add_child(v)
            return self

class Item:
    def __init__(self):
        self.node = None

class HollowHeap:

    # make-heap method
    def __init__(self):
        self.h = None
        self.A = {}
        self.max_rank = None

    def insert(self, e: Item, k: int):
        self.h = self.meld(Node(e, k))
        return self.h

    def meld(self, g: Node):
        if g == None:
            return self.h
        if self.h == None:
            return g
        return self.link(g)

    def find_min(self):
        if self.h == None:
            return None
        else:
            return self.h.item

    def decrease_key(self, e: Item, k: int):
        u = e.node
        if u == self.h:
            u.key = k
            return self.h
        v = Node(e, k)
        u.item = None
        if u.rank > 2:
            v.rank = u.rank - 2
        v.child = u
        u.ep = v
        self.h = self.link(v)
        return self.h

    def delete_min(self):
        return self.delete(self.h.item)

    def link(self, v: Node):
        if self.h.key >= v.key:
            v.add_child(self.h)
            return v
        else:
            self.h.add_child(v)
            return self.h

    def delete(self, e: Item):
        self.A = dict()
        e.node.item = None
        e.node = None
        # Non-minimum deletion
        if self.h != None and self.h.item != None:
            return self.h
        self.max_rank = 0
        # While list L of hollow roots is not empty
        while self.h != None:
            w = self.h.child
            v = self.h
            self.h = self.h.next
            while w != None:
                u = w
                w = w.next
                if u.item == None:
                    if u.ep == None:
                        u.next = self.h
                        self.h = u
                    else:
                        if u.ep == v:
                            w = None
                        else:
                            u.next = None
                        u.ep = None
                else:
                    self.do_ranked_links(u)
        self.do_unranked_links()
        if self.h != None:
            self.h.next = None
        return self.h

    def do_ranked_links(self, u: Node):
        while u.rank in self.A and self.A[u.rank] != None:
            u = u.link(self.A[u.rank])
            self.A[u.rank] = None
            u.rank += 1
        self.A[u.rank] = u
        if u.rank > self.max_rank:
            self.max_rank = u.rank
    
    def do_unranked_links(self):
        for i in range(self.max_rank + 1):
            if i in self.A and self.A[i] != None:
                if self.h == None:
                    self.h = self.A[i]
                else:
                    self.h = self.h.link(self.A[i])
                self.A[i] = None
