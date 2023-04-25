def karat_binary(x, y):
    # Base case: if x or y is less than 10, return the simple product
    if x < 10 or y < 10:
        return x * y
    
    # Determine the size of the split
    split = min(len(bin(x)) - 2, len(bin(y)) - 2) >> 1
    
    # Calculate a bitmask of ones of length split
    ones = (1 << split) - 1
    
    # Split x and y into upper and lower halves
    x1 = x >> split
    x0 = x & ones
    y1 = y >> split
    y0 = y & ones
    
    # Recursively compute the three intermediate products
    x0y0 = karat_binary(x0, y0)
    x1y1 = karat_binary(x1, y1)
    part34 = karat_binary(x1 + x0, y1 + y0)
    
    # Compute the final product using the Karatsuba formula
    t1 = x1y1 << (split << 1)
    t2 = (part34 - x1y1 - x0y0) << split
    return t1 + t2 + x0y0

# Test the function with some example inputs
x = 587543354358537525345742
y = 1652482445274257
print(karat_binary(x, y))
print(x * y)  # Verify that the output is correct
