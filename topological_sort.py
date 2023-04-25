from collections import defaultdict, deque

def topological_sort(vertices, adj_lst):
    # Get the total number of vertices in the graph
    n = len(vertices)
    
    # Compute the in-degree of each vertex
    in_degree = defaultdict(int)
    for i in adj_lst:
        for j in adj_lst[i]:
            in_degree[j] += 1
    
    # Initialize a queue with all vertices that have an in-degree of 0
    queue = deque()
    for i in adj_lst:
        if in_degree[i] == 0:
            queue.append(i)
    
    # Initialize a counter for the number of vertices in the topological order
    cnt = 0
    
    # Initialize an empty list for the topological order
    top_order = []
    
    # Apply Kahn's algorithm
    while queue:
        # Remove a vertex with an in-degree of 0 from the queue
        u = queue.popleft()
        
        # Add the vertex to the topological order
        top_order.append(u)
        
        # Decrement the in-degree of all adjacent vertices
        for i in adj_lst[u]:
            in_degree[i] -= 1
            # If a vertex's in-degree becomes 0, add it to the queue
            if in_degree[i] == 0:
                queue.append(i)
        
        # Increment the counter for the number of vertices in the topological order
        cnt += 1
    
    # Check if the number of vertices in the topological order is equal to the total number of vertices
    # If not, there is a cycle in the graph
    if cnt != n:
        return "There is a cycle in the graph"
    else:
        return top_order


# Example usage
adj_lst = defaultdict(list)
vertices = ['Programming','Algorithm', 'AI', 'Network', 'Web development']
adj_lst['Programming'].append('Algorithm')
adj_lst['Algorithm'].append('AI')
adj_lst['Programming'].append('Web development')
adj_lst['Network'].append('Web development')
print(topological_sort(vertices, adj_lst))
