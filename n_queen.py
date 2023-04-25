# Define a recursive function to solve the n-queens problem
def n_queen(lst, ind, n):
    # Base case: if all queens have been placed, return the solution
    if ind == n:
        return lst
    # Try placing the queen in each column of the current row
    for i in range(n):
        # Check if the queen conflicts with any previously placed queens
        if i in lst[:ind]: # check if the queen is already in the same column
            continue
        for j in range(ind):
            # check if the queen is on the same diagonal as any of the previously placed queens
            if abs(j - ind) == abs(lst[j] - i):
                break
        else: # if the queen doesn't conflict with any previously placed queens
            lst[ind] = i
            # Recursively solve the subproblem of placing the remaining queens
            res = n_queen(lst, ind + 1, n)
            if res != False:
                return res # if a solution is found, return it
    return False # if no solution is found, backtrack and try another column for the current row

# Get the input value of n from the user
n = int(input())
# Solve the n-queens problem and store the result in a list
temp = n_queen([-1 for _ in range(n)], 0, n)
# Print the final solution as a chessboard with queens represented by '*' and empty squares represented by '.'
for i in range(n):
    x = ['.' for _ in range(n)]
    x[temp[i]] = '*'
    print(' '.join(x))
