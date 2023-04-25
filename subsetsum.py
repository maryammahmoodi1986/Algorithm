# Define a function to find the closest sum of items in a set S that add up to a target volume t
def exact_exponential_time(S, t):
    L = {0}  # Initialize a set with a single element 0
    for a in S:
        temp = set()
        for x in L:
            if x + a <= t:
                temp.add(x + a)
        L |= temp  # Union the sets L and temp to add the new sums to L
    return max(L)  # Return the largest sum in L that is <= t

# Test the exact_exponential_time function with a sample input
print(exact_exponential_time([2, 3, 5, 7], 16))


# Define a function to trim a set of numbers by removing elements that are too close to each other
def trim(L, gamma):
    gamma += 1  # Increase gamma by 1 to account for the fact that we are dealing with integer division
    Y = sorted(L)  # Sort the input set
    L_p = [Y[0]]  # Initialize a new set L_p with the smallest element of Y
    for x in Y:
        if x > L_p[-1] * gamma:  # If x is farther from the previous element in L_p than gamma, add it to L_p
            L_p.append(x)
    return set(L_p)  # Return the trimmed set as a set (i.e., with no duplicates)

# Test the trim function with a sample input
print(trim([10, 11, 12, 15, 20, 21, 22, 23, 24, 29], 0.1))


# Define a function to approximate the closest sum of items in a set S that add up to a target volume t,
# using the trim function to reduce the size of the search space
def approximate_polynomial(S, t, eps):
    L = {0}  # Initialize a set with a single element 0
    gamma = eps / (2 * len(S))  # Compute gamma based on the input set S and the desired error epsilon
    for a in S:
        temp = set()
        for x in L:
            if x + a <= t:
                temp.add(x + a)
        L = trim(L | temp, gamma)  # Union the sets L and temp, trim the result with gamma, and update L
    return L, max(L)  # Return the trimmed set L and the largest sum in L that is <= t

# Test the approximate_polynomial function with a sample input
print(approximate_polynomial([1, 3, 4, 5, 7, 8], 15, 0.9))
