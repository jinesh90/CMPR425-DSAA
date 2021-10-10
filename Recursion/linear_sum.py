"""
get the sum of sequence by using recursion
"""

def seq_sum(array, n):
    if n == 0:
        return 0
    else:
        return seq_sum(array, n-1) + array[n-1]


print(seq_sum([1, 2, 3, 4, 5, 6], 6))
