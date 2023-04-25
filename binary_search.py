# Define a function binary_search that takes a sorted list (lst), a key to search for, and the indices of the beginning (b) and end (e) of the subsection of lst to search
def binary_search(lst, key, b, e):
    # If the subsection is empty (b > e), the key is not in the list
    if b > e:
        return False
    
    # Calculate the middle index of the subsection
    m = (e + b) // 2
    
    # If the key is found at the middle index, return the index
    if key == lst[m]:
        return m
    
    # If the key is less than the middle element, recursively search the left half of the subsection
    elif key < lst[m]:
        return binary_search(lst, key, b, m )
    
    # If the key is greater than the middle element, recursively search the right half of the subsection
    else:
        return binary_search(lst, key, m + 1, e)

# Create a sorted list and test the binary_search function on each element of the list
lst = [1, 2, 3, 4, 5, 6, 7, 8]
for x in lst:
    print(binary_search(lst, x, 0, len(lst) - 1))
