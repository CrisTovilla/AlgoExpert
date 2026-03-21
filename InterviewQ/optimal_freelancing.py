def optimalFreelancing(jobs):
    # Write your code here.
    WEEK_LENGHT = 7
    schedule = [False] * 7
    jobs = sorted(jobs, key=lambda item: item["payment"], reverse=True)
    profit = 0
    for job in jobs:
        deadline = min(job["deadline"], WEEK_LENGHT)
        for idx in reversed(range(deadline)):
            if schedule[idx] == False:
                schedule[idx] = True
                profit = profit + job["payment"]
                break
    return profit
