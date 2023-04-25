def scheduling(weights, lengths):
    # Sort tasks based on weight/length ratio in descending order
    data = sorted(zip(weights, lengths, range(len(weights))), key=lambda x: x[0] / x[1], reverse=True)
    
    # Initialize variables
    total_cost = 0
    completion = 0
    seq = []
    
    # Iterate through tasks and calculate total cost and completion time
    for i in range(len(data)):
        seq.append(data[i][2]) # record the index of the scheduled task
        completion += data[i][1] # add the length of the current task to the completion time
        total_cost += completion * data[i][0] # add the cost of the current task to the total cost
    
    # Return total cost and sequence of tasks
    return total_cost, seq


# Example usage
weights = [1, 1, 5, 3]
lengths = [2, 4, 2, 1]
print(scheduling(weights, lengths))

