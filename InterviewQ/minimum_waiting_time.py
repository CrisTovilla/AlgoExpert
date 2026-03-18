def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    waiting_time = 0
    accumulator = 0
    for i in range(len(queries) - 1):
        accumulator += queries[i]
        waiting_time += accumulator
    return waiting_time
