# Define a Node class that represents a node in the heap. Each node has a key and a value.
class Node:
    def __init__(self, k, v):
        self.key = k  # cost to node
        self.value = v  # related edge

    def __lt__(self, other):
        return self.key < other.key
    
    def __str__(self):
        return f'{self.key}, {self.value}'

# Define a Heap class that represents a min-heap data structure. The heap is implemented as a list of nodes.
class Heap:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def parent(self, j):
        return (j - 1) // 2
    
    def is_empty(self):
        return len(self) == 0
    
    def left(self, j):
        return 2 * j + 1
    
    def right(self, j):
        return 2 * j + 2
    
    def has_left(self, j):
        return self.left(j) < len(self)
    
    def has_right(self, j):
        return self.right(j) < len(self)
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def up
# Define a function dijkstra that takes an adjacency list adj_lst and a source node src, and returns a dictionary of shortest paths from the source node to each node in the graph.
def dijkstra(adj_lst, src):
    shortest_paths = {}  # Initialize an empty dictionary to store the shortest paths from the source node
    heap = Heap()  # Create a new heap
    node_locator = {}  # Create a dictionary to store the nodes in the heap
    for v in adj_lst:
        if v == src:
            cost = 0
        else:
            cost = float('inf')
        node_locator[v] = heap.add(cost, (None, v))  # Add each node to the heap with the cost set to infinity, except for the source node which has cost 0.
    while not heap.is_empty():  # While the heap is not empty
        cost, edge = heap.extract_min()  # Extract the node with the minimum cost from the heap
        n1, n2 = edge  # Get the two nodes in the edge
        path_to_n2 = shortest_paths.get(n1, [''])[0] + n2  # Get the path to n2 from the source node
        shortest_paths[n2] = [path_to_n2, cost]  # Update the shortest path to n2 in the dictionary
        for v, w in adj_lst[n2].items():  # For each neighbor v of n2
            if v in node_locator and node_locator[n2].key + w < node_locator[v].key:  # If the cost to reach v through n2 is less than its current cost in the heap
                heap.update(node_locator[v], node_locator[n2].key + w, (n2, v))  # Update the cost of v in the heap
    return shortest_paths  # Return the dictionary of shortest paths

# Define an adjacency list for the graph, and call the dijkstra function with the source node 's'
adj_lst = {'s': {'v': 1, 'w': 4},
           'v': {'w': 2, 't': 6},
           'w': {'t': 3},
           't': {}}
print(dijkstra(adj_lst, 's'))
