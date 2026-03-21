def getNthFib(n):
    # Write your code here.
    n1,n2 = -1, 1
    for _ in range(n):
        n1, n2 = n2, n1 + n2
    return n2
