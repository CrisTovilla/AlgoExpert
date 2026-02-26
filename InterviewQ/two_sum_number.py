def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1
    while(left < right):
        total = array[left] + array[right]
        if total == targetSum:
            return [array[left],array[right]]
        elif total < targetSum:
            left = left + 1
        else:
            right = right - 1
    return []
