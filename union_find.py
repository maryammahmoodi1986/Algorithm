class Leader:
    # Each Leader object represents a set with one element
    # It has a size of 1 and is its own parent (root)
    def __init__(self):
        self.size = 1
        self.parent = self


class UnionFind:
    # The UnionFind class represents a collection of disjoint sets
    # It allows two sets to be merged (union) and finds the set that an element belongs to (find)

    def union(self, p, q):
        # Merge the sets that contain p and q
        a = self.find(p)
        b = self.find(q)
        if a is b: 
            return False  # p and q are already in the same set
        if a.size < b.size:
            a, b = b, a  # merge the smaller set into the larger set
        b.parent = a  # make the parent of b point to a (merge the sets)
        a.size += b.size  # update the size of the merged set (union by size)
        return True

    def find(self, x):
        # Find the set that x belongs to (by finding its root)
        if x == x.parent:
            return x  # x is the root of its set
        x.parent = self.find(x.parent)  # path compression: make x's parent point to the root
        return x.parent

