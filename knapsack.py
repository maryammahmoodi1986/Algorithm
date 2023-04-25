def knapsack(W, n, items):
    # Create a 2D list of size (n+1) x (W+1) initialized with 0
    K = [[0 for i in range(W + 1)] for j in range(n + 1)]
    
    # Fill in the table using dynamic programming
    for i in range(1, n + 1):
        for w in range(W + 1):
            # Calculate the remaining weight when choosing item i with capacity w
            t = w - items[i - 1]['weight']
            # Calculate the value of the knapsack with and without item i
            new_val = K[i - 1][t] + items[i - 1]['value'] if t >= 0 else 0
            # Choose the maximum value between the two options
            K[i][w] = max(K[i - 1][w], new_val)
    
    # Return the maximum value of the knapsack and the entire table
    return K[n][W], K

# Example usage
W, n = 7, 3
items = [{'value': 3, 'weight': 8},
         {'value': 5, 'weight': 4},
         {'value': 6, 'weight': 2}]
best, all_res = knapsack(W, n, items)

# Print the table
print('\t', *[f'w{i}' for i in range(W + 1)], sep='\t')
for i in range(n + 1):
    print(f'obj{i}', *all_res[i], sep='\t')
