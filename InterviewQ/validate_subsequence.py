def isValidSubsequence(array, sequence):
    # Write your code here.
    sequence_index = 0
    for number in array:
        if sequence_index >= len(sequence):
            break
        if number == sequence[sequence_index]:
            sequence_index = sequence_index + 1
    if sequence_index == len(sequence):
        return True
    else:
        return False
