def karatsuba(x,y):
    if x < 10 or y < 10:  # base case, if either x or y has only one digit
        return x * y
    else:
        split = max(len(str(x)), len(str(y))) // 2  # split the digits of x and y equally
        base = 10 ** split  # set the base for the split digits
        a, b = divmod(x, base)  # split x into a and b
        c, d = divmod(y, base)  # split y into c and d
        p1 = karatsuba(a, c)  # recursive call for a*c
        p2 = karatsuba(b, d)  # recursive call for b*d
        p3 = karatsuba(a + b, c + d)  # recursive call for (a+b)*(c+d)
        p4 = p3 - p2 - p1  # compute p4 = (a+b)*(c+d) - p1 - p2
        return p1 * 10 ** (2 * split) + p2 + (p4 * base)  # compute the final result

aa = 112
bb = 117867861545706958453625413526347577898765
print(aa * bb)  # compute the correct result using standard multiplication
print(karatsuba(aa, bb))  # compute the result using Karatsuba algorithm
