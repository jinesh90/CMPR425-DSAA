"""
leet code 704
"""


def binary_search(nums, target):
    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return -1


print(binary_search([5], 5))

