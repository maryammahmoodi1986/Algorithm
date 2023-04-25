# Define a function counting_sort that takes a list A of integers to be sorted, and a parameter k that represents the maximum value in A
def counting_sort(A, k):
    # Initialize an empty list B that will be used to store the sorted list
    B = [0 for _ in range(len(A))]
    
    # Initialize an empty list C that will be used as a temporary array to count the occurrences of each value in A
    C = [0 for _ in range(k + 1)]
    
    # For each element x in A, increment the corresponding counter in C
    for x in A:
        C[x] += 1
    
    # Update each counter in C to be the sum of itself and the previous counter, so that C[i] contains the number of elements in A that are less than or equal to i
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    
    # Iterate over each element of A in reverse order, and for each element A[i], place the element in the correct position in B using the counter array C
    for i in range(len(A)): # for being stable, start from len(A)-1
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    
    # Return the sorted list B
    return B

# Test the function with the input [2,1,2,1] and k=2, and print the result
print(counting_sort([2,1,2,1], 2))

# Generate a list of numbers from 1 to 49, shuffle it 100 times, and assert that the output of counting_sort() is equal to the output of Python's built-in sorted() function
from random import shuffle
lst = list(range(1, 50))
for i in range(100):
    shuffle(lst)
    assert counting_sort(lst, max(lst)) == sorted(lst)
