def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1
    while(left <= right):
        mid = (left + right) // 2
        value = array[mid]
        if value == target:
            return mid
        elif value > target:
            right = mid - 1
        elif value < target:
            left = mid + 1
    return -1
