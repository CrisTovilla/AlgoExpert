def findThreeLargestNumbers(array):
    # Write your code here.
    largest = [None, None, None]
    for number in array:
        last_i = None
        for i in range(len(largest)-3,len(largest)):
            if not largest[i] or number > largest[i]:
                last_i = i + 1
        if last_i is not None:
            largest.insert(last_i, number) 
    return largest[-3:]
