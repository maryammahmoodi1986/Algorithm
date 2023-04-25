class Node:
    def __init__(self, k, v):
        self.key = k  # cost to node
        self.value = v  # related edge

    def __lt__(self, other):
        return self.key < other.key

class Heap:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def parent(self, j):
        return (j - 1) // 2

    def is_empty(self):
        return len(self) == 0

    def left(self, j):
        return 2 * j + 1

    def right(self, j):
        return 2 * j + 2

    def has_left(self, j):
        return self.left(j) < len(self)

    def has_right(self, j):
        return self.right(j) < len(self)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def upheap(self, j):
        parent = self.parent(j)
        if j > 0 and self.data[j] < self.data[parent]:
            self.swap(j, parent)
            self.upheap(parent)

    def downheap(self, j):
        if self.has_left(j):
            left = self.left(j)
            small_child = left
            if self.has_right(j):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self.downheap(small_child)

    def add(self, key, value):
        token = Node(key, value)
        self.data.append(token)
        self.upheap(len(self.data) - 1)
        return token

    def remove_min(self):
        self.swap(0, len(self.data) - 1)
        item = self.data.pop()
        self.downheap(0)
        return item.key, item.value

    def update(self, loc, new_key, new_val):
        loc.key = new_key
        loc.value = new_val
        j = self.data.index(loc)
        if j > 0 and self.data[j] < self.data[self.parent(j)]:  # not root and less than parent
            self.upheap(j)  # check above j
        else:  # up is ok, look below j
            self.downheap(j)

    def delete(self, loc):
        ...


def heap_sort(lst):
    h = Heap()
    for x in lst:
        h.insert(x, x)  # add each element to the heap with key and value equal to the element
    sorted_lst = []
    for _ in range(len(lst)):
        sorted_lst.append(h.extract_min())  # extract minimum element and append to sorted list
    return sorted_lst


from random import shuffle

a = list(range(20))
shuffle(a)
print(heap_sort(a))  # shuffle list, sort with heap_sort and print sorted list

