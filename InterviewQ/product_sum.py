def _handle_array(array, depth, total):
    for item in array:
        if not isinstance(item, list):
            total = total + item
        else:
            total = total + _handle_array(item, depth + 1, 0)
    return total * depth
        

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    total = _handle_array(array, 1, 0)
    return total
