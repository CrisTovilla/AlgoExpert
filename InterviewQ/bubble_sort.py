def bubbleSort(array):
    # Write your code here.
    swapped = True
    counter = 0
    while(swapped):
        swapped = False
        for i in range(len(array) - 1 - counter):
            current = array[i]
            next = array[i + 1]
            if current > next:
                array[i + 1] = current
                array[i] = next
                swapped = True
        counter = counter + 1
    return array
