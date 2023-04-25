def partition(A, l, r):
    pivot = l   # select the leftmost element as the pivot
    p = A[l]    # set the pivot value
    i = l + 1   # initialize the index i
    for j in range(l + 1, r + 1):
        if A[j] <= p:   # if the current element is less than or equal to the pivot
            A[i], A[j] = A[j], A[i]   # swap the elements at i and j
            i += 1    # increment i
    A[pivot], A[i - 1] = A[i - 1], A[pivot]   # swap the pivot with the element at index i-1
    return i - 1   # return the index of the pivot

def quick_sort(A, l, r):
    if l >= r:   # if there is only one element or less in the subarray, return
        return
    p = partition(A, l, r)   # partition the subarray and get the index of the pivot
    quick_sort(A, l, p - 1)   # recursively quicksort the subarray to the left of the pivot
    quick_sort(A, p + 1, r)   # recursively quicksort the subarray to the right of the pivot

lst = [3, 2, 1]
quick_sort(lst, 0, len(lst) - 1)   # sort the list using quicksort
print(lst)   # output the sorted list

