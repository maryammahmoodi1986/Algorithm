class Leader:
    def __init__(self):
        self.size = 1
        self.parent = self


class UnionFind:
    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)
        if a is b:  # if p and q are already in the same set
            return False
        # Merge the smaller set into the larger set, and update the size of the larger set
        if a.size < b.size:
            a, b = b, a
        b.parent = a
        a.size += b.size  # union by size
        return True

    def find(self, x):
        if x == x.parent:  # if x is the leader of its set
            return x
        # Use path compression to recursively update the parent of x to the leader of its set
        x.parent = self.find(x.parent)
        return x.parent


def adjacency_to_edge(adj_lst):
    edges = {}
    for u, neighbors in adj_lst.items():
        for v, weight in neighbors.items():
            if (u, v) not in edges or (v, u) not in edges:  # assume not directed
                edges[(u, v)] = weight
    return edges


def kruskal(adj_lst):
    # Convert the adjacency list to a dictionary of edges and their weights
    edges = adjacency_to_edge(adj_lst)
    mst = []  # minimum spanning tree
    uf = UnionFind()  # create a UnionFind data structure
    leaders = {}  # dictionary to store the leader of each vertex's set
    cost = 0  # total cost of the minimum spanning tree
    for v in adj_lst:
        leaders[v] = Leader()  # initialize each vertex as the leader of its own set
    # Sort the edges by weight in non-descending order
    edges = sorted(edges.items(), key=lambda x: x[1])
    k = 0
    # Iterate over the edges in the sorted order, adding them to the minimum spanning tree if they don't create a cycle
    while len(mst) < len(adj_lst) - 1:
        edge, weight  = edges[k]
        k += 1
        u, v = edge
        # If u and v are not in the same set, merge their sets and add the edge to the minimum spanning tree
        if uf.union(leaders[u], leaders[v]):
            cost += weight
            mst.append(f'{u}->{v}')
    return cost, mst


# Example usage
adjacency_lst = {'A': {'B': 2, 'C': 4},
                 'B': {'A': 2, 'C': 1, 'D': 1, 'E': 1},
                 'C': {'A': 4, 'B': 1, 'E': 8},
                 'D': {'B': 1, 'F': 7},
                 'E': {'B': 1, 'C': 8, 'F': 2},
                 'F': {'D': 7, 'E': 2}}
print(kruskal(adjacency_lst))
