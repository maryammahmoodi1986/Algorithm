# Define a Node class to represent vertices in the graph
class Node:
    def __init__(self, key):
        self.key = key
        self.is_visited = False
        self.dist = 0

# Define a breadth-first search function
def bfs(root):
    # Set the root vertex as visited and its distance as 0
    vertices[root].is_visited = True
    vertices[root].dist = 0
    # Initialize a queue with the root vertex
    q = [root]
    while q:
        # Dequeue the next vertex from the queue
        u = q.pop(0)
        # Visit all the neighbors of u
        for v in edges[u]:
            if not vertices[v].is_visited:
                # If v has not been visited yet, mark it as visited
                # and set its distance to u's distance + 1
                vertices[v].is_visited = True
                vertices[v].dist = vertices[u].dist + 1
                # Enqueue v for further processing
                q.append(v)
        # Print the vertex and its distance from the root
        print(u, vertices[u].dist)

# Define a depth-first search function
def dfs(root):
    # Set the root vertex as visited and its distance as 0
    vertices[root].is_visited = True
    vertices[root].dist = 0
    # Initialize a stack with the root vertex
    q = [root]
    while q:
        # Pop the next vertex from the stack
        u = q.pop()
        # Visit all the neighbors of u
        for v in edges[u]:
            if not vertices[v].is_visited:
                # If v has not been visited yet, mark it as visited
                # and set its distance to u's distance + 1
                vertices[v].is_visited = True
                vertices[v].dist = vertices[u].dist + 1
                # Push v onto the stack for further processing
                q.append(v)
        # Print the vertex and its distance from the root
        print(u, vertices[u].dist)

# Define a function to reverse the lines in a file
def reverse_file(file_name):
    # Initialize a deque to store the lines in the file
    s = deque()
    # Read the lines from the file and add them to the deque
    for line in open(file_name):
        s.append(line.strip())
    # Write the lines from the deque back to the file in reverse order
    with open(file_name, 'w') as file:
        while s:
            file.write(s.pop() + '\n')
            
            

'''
G           H
|           |   
C - A - B - D
|           |
E           F
'''
vertices = {'A': Node('A'),
            'B': Node('B'),
            'C': Node('C'),
            'D': Node('D'),
            'E': Node('E'),
            'F': Node('F'),
            'G': Node('G'),
            'H': Node('H'), }
edges = {'A': ['B', 'C'],
         'B': ['A', 'D'],
         'C': ['A', 'E', 'G'],
         'D': ['B', 'F', 'H'],
         'E': ['C'],
         'F': ['D'],
         'G': ['C'],
         'H': ['D']}
bfs('A')

reverse_file('file.txt')


