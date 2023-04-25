# Define a function to merge two sorted subarrays
def merge(A, p, q, r):
    # Create left and right subarrays with a sentinel value of infinity at the end
    L = A[p: q + 1] + [float('inf')]
    R = A[q + 1: r + 1] + [float('inf')]
    i = 0
    j = 0
    # Merge the left and right subarrays into the original array in sorted order
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

# Define a function to recursively sort an array using merge sort
def merge_sort(A, p, r):
    if p < r:
        # Find the middle index of the array
        q = (p + r) // 2
        # Recursively sort the left and right halves of the array
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        # Merge the sorted left and right halves of the array
        merge(A, p, q, r)

# Create a list of integers and shuffle it
lst = list(range(1, 21))
shuffle(lst)
print(lst)
# Sort the list using merge sort and print the sorted list
merge_sort(lst, 0, len(lst) - 1)
print(lst)
