# Node class to store the cost and related edge
class Node:
    def __init__(self, k, v):
        self.key = k  # cost to node
        self.value = v  # related edge

    # Define less than operator to compare based on cost
    def __lt__(self, other):
        return self.key < other.key

# Heap class to store the nodes in a min-heap
class Heap:
    def __init__(self):
        self.data = []

    # Define length operator to get the number of nodes in the heap
    def __len__(self):
        return len(self.data)

    # Helper function to get the parent index of a node
    def parent(self, j):
        return (j - 1) // 2

    # Helper function to check if the heap is empty
    def is_empty(self):
        return len(self) == 0

    # Helper functions to get the left and right child indices of a node
    def left(self, j):
        return 2 * j + 1

    def right(self, j):
        return 2 * j + 2

    # Helper functions to check if a node has a left or right child
    def has_left(self, j):
        return self.left(j) < len(self)

    def has_right(self, j):
        return self.right(j) < len(self)

    # Helper function to swap two nodes in the heap
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    # Helper function to move a node up in the heap to maintain heap property
    def upheap(self, j):
        parent = self.parent(j)
        if j > 0 and self.data[j] < self.data[parent]:
            self.swap(j, parent)
            self.upheap(parent)

    # Helper function to move a node down in the heap to maintain heap property
    def downheap(self, j):
        if self.has_left(j):
            left = self.left(j)
            small_child = left
            if self.has_right(j):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self.downheap(small_child)

    # Function to add a new node to the heap
    def add(self, key, value):
        token = Node(key, value)
        self.data.append(token)
        self.upheap(len(self.data) - 1)
        return token

    # Function to remove the minimum-cost node from the heap
    def remove_min(self):
        self.swap(0, len(self.data) - 1)
        item = self.data.pop()
        self.downheap(0)
        return item.key, item.value

    # Function to update the cost and related edge of a node in the heap
    def update(self, loc, new_key, new_val):
        loc.key = new_key
        loc.value = new_val
        j = self.data.index(loc)
        if j > 0 and self.data[j] < self.data[self.parent(j)]:  # not root and less than parent
            self.upheap(j)  # check above j
        else:  # up is ok, look below j
            self.downheap(j)

# Function to find the minimum spanning tree using Prim's algorithm
def prim(adj_lst):
    all_cost = 0
    mst = []  # final solution
    pq = Heap()  # priority queue to store the nodes
    pq_locator = {}  # dictionary to map nodes to their corresponding Node instances in the priority queue, for fast accessing

    # Add all vertices to the priority queue, with the first one having cost 0
    for v in adj_lst:
        cost = 0 if len(pq_locator) == 0 else float('inf')
        pq_locator[v] = pq.add(cost, (None, v))

    # Repeat until all nodes are visited
    while not pq.is_empty():
        cost, edge = pq.remove_min()
        all_cost += cost
        n1, n2 = edge
        mst.append(f'{n1}->{n2}')
        del pq_locator[n2]
        # Update the cost and related edge of each neighbor of the current node in the priority queue
        for v, w in adj_lst[n2].items():
            if v in pq_locator and w < pq_locator[v].key:
                pq.update(pq_locator[v], w, (n2, v))

    return all_cost, mst[1:]  # Return the total cost and the edges in the minimum spanning tree

# Sample adjacency list for testing
adj_lst = {'A': {'B': 2, 'C': 4},
           'B': {'A': 2, 'C': 1, 'D': 1, 'E': 1},
           'C': {'A': 4, 'B': 1, 'E': 8},
           'D': {'B': 1, 'F': 7},
           'E': {'B': 1, 'C': 8, 'F': 2},
           'F': {'D': 7, 'E': 2}}

# Call the prim() function on the adjacency list and print the result
print(prim(adj_lst))
