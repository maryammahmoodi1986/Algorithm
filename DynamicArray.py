import ctypes

class DynamicArray:

    def make_array(self, c):
        # helper function to create an array of c elements, initialized to None
        return (c * ctypes.py_object)()

    def __init__(self):
        # initialize the dynamic array with 0 elements and a capacity of 1
        self.n = 0
        self.capacity = 1
        # create the underlying array with the initial capacity of 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        # return the number of elements currently in the array
        return self.n

    def append(self, obj):
        # if the number of elements in the array equals the capacity, resize the array
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        # add the new element at the end of the array and increment the number of elements
        self.A[self.n] = obj
        self.n += 1

    def resize(self, c):
        # create a new array with capacity c
        B = self.make_array(c)
        # copy the existing elements to the new array
        for k in range(self.n):
            B[k] = self.A[k]
        # replace the old array with the new one and update the capacity
        self.A = B
        self.capacity = c

    def __str__(self):
        # return a string representation of the array
        s = '<'
        for x in range(self.n-1):
            s += f'{self.A[x]},'
        return s + f'{self.A[self.n-1]}>'

    def __getitem__(self, k):
        # get the element at index k
        if not 0 <= k < self.n:
            raise IndexError
        return self.A[k]

# create a new dynamic array and append some elements to it
d = DynamicArray()
d.append(2)
d.append(3)
d.append(5)

# test the 'in' operator and print the array
print(2 in d)
print(d)

