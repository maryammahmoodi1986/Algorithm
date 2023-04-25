import random   # import the random module

def randomized_selection(A, l, r, ind):
    if l - r == 1:   # if there is only one element in the subarray, return it
        return A[l]
    pivot = random.randint(l, r)   # choose a random pivot index
    A[pivot], A[l] = A[l], A[pivot]   # swap the pivot with the leftmost element
    p = A[l]   # set the pivot value
    i = l + 1   # initialize the index i
    for j in range(l + 1, r + 1):
        if A[j] <= p:   # if the current element is less than or equal to the pivot
            A[i], A[j] = A[j], A[i]   # swap the elements at i and j
            i += 1    # increment i
    A[l], A[i - 1] = A[i - 1], A[l]   # swap the pivot with the element at index i-1
    j = i - 1
    if j - l == ind:   # if the index of the pivot is the desired index, return the pivot value
        return A[j]
    if j - l  > ind:   # if the index of the pivot is greater than the desired index, recurse on the left subarray
        return randomized_selection(A, l, j - 1, ind)
    if j - l  < ind:   # if the index of the pivot is less than the desired index, recurse on the right subarray
        return randomized_selection(A, j + 1, r, ind - (1+j-l))

# Test the function with a range of indices
for k in range(4):
    lst = [25, 65, 35, 45]
    print(randomized_selection(lst, 0, len(lst) - 1, k))   # output the kth smallest element in the list
