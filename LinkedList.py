class Node:
    def __init__(self, k):
        self.key = k
        self.prev = None

class LinkedListStack:
    def __init__(self):
        self.last = None

    def is_empty(self):
        return self.last == None

    def push(self, k):
        n = Node(k)
        if not self.last:
            self.last = n
        else:
            n.prev = self.last
            self.last = n

    def pop(self):
        if self.last:
            deleted = self.last
            self.last = self.last.prev
            return deleted.key
        else:
            raise Exception('Stack is empty')

def check_parenthesis(s):
    # Create an instance of the LinkedListStack class to use as a stack
    stack = LinkedListStack()

    # Define a dictionary with the closing brackets as keys and the opening brackets as values
    d = {')': '(', ']': '[', '}': '{'}

    # Iterate over each character in the string
    for x in s:
        # If the character is an opening bracket, push it onto the stack
        if x in d.values():
            stack.push(x)
        # If the character is a closing bracket, pop the top element from the stack and check if it matches the corresponding opening bracket
        elif x in d.keys():
            if stack.is_empty():
                return False
            u = stack.pop()
            if d[x] != u:
                return False

    # After iterating over all characters, if the stack is empty, the parentheses are balanced
    return stack.is_empty()

# Test the check_parenthesis function with some examples
print(check_parenthesis('{3: (a[1]+a[2]) / 2}')) # True
print(check_parenthesis('[)]')) # False
print(check_parenthesis('[)')) # False
print(check_parenthesis('](}')) # False
