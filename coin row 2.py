# Define a function coin_row that takes a list of integers representing the values of coins in a row
def coin_row(c):
    # Store the length of the list in n
    n = len(c)
    
    # Insert a None element at the beginning of the list to make indexing more convenient
    c.insert(0, None)
    
    # Initialize a list f with the base cases f[0] = 0 and f[1] = c[1], which represent the maximum possible sum when choosing 0 or 1 coins, respectively
    f = [0, c[1]]
    
    # For each index i from 2 to n, compute the maximum possible sum of coins up to index i using the recurrence relation f[i] = max(c[i] + f[i - 2], f[i - 1]), which considers two cases: either the coin at index i is chosen, in which case the maximum sum up to index i is the sum of the coin at index i and the maximum sum up to index i - 2 (since no two adjacent coins can be chosen), or the coin at index i is not chosen, in which case the maximum sum up to index i is the same as the maximum sum up to index i - 1
    for i in range(2, n + 1):
        f.append(max(c[i] + f[i - 2], f[i - 1]))
    
    # Return the maximum possible sum of coins, which is given by f[n]
    return f[n]

# Test the function with the example input [5, 1, 2, 10, 6, 2], which represents a row of coins with values 5, 1, 2, 10, 6, and 2
print(coin_row([5, 1, 2, 10, 6, 2]))
