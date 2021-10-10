"""
Binary search algorithm for searching element from array.
Recursion
"""


def binary_search(array, target, low, high):
    # base case
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            return binary_search(array, target, low, mid-1)
        else:
            return binary_search(array, target, mid+1, high)



# a = [1,2,3,4,5,10,20,40,80,160]
# print(binary_search(a, 0, 0, len(a)-1))

