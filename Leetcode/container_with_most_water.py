"""
leetcode 11. find container with the most water.
"""


def container_with_most_water(height):
    max_area = 0
    i = 0
    j = len(height) - 1
    while i < j:
        left_height = height[i]
        right_height = height[j]
        area = min(left_height, right_height) * (j - i)
        if area >= max_area:
            max_area = area
        if left_height >= right_height:
            j = j - 1
        else:
            i = i + 1
    return max_area

a = [1,8,6,2,5,4,8,3,7]


print(container_with_most_water(a))
