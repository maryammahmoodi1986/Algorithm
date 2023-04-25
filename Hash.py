from random import randrange

class Hash:
    def __init__(self):
        # Initialize number of elements and capacity to 0 and 10 respectively
        self.n = 0
        self.capacity = 10
        # Initialize the data structure as a list of 10 empty lists
        self.data = [[] for _ in range(self.capacity)]

    def hash(self, x):
        # Compute the hash value of an element using modulo
        return x % self.capacity

    def add(self, x):
        # Compute the hash index of the element
        ind = self.hash(x)
        # If the element is not in the list, add it and update element count
        if x not in self.data[ind]:
            self.data[ind].append(x)
            self.n += 1
            # Check the load factor and resize if necessary
            self.check()

    def remove(self, x):
        # Compute the hash index of the element
        ind = self.hash(x)
        # Try to remove the element from the list at the hash index
        try:
            self.data[ind].remove(x)
        except:
            # If the element is not in the list, do nothing
            pass

    def check(self):
        # Compute the load factor of the hash table
        load_factor = self.n / self.capacity
        # If the load factor exceeds 0.75, resize the hash table and rehash elements
        if load_factor > 0.75:
            self.capacity *= 2
            temp = []
            for row in self.data:
                temp += row
            self.data = [[] for _ in range(self.capacity)]
            for x in temp:
                self.add(x)

    def __contains__(self, item):
        # Compute the hash index of the element and check if it's in the list
        ind = self.hash(item)
        return item in self.data[ind]

