"""
leet code problem 42
dynamic programming method
"""


def find_tapping_water(height):
    ans = 0
    if len(height) == 0:
        return 0
    left_max = [None] * len(height)
    right_max = [None] * len(height)
    left_max[0] = height[0]
    for i in range(1, len(height)):
        left_max[i] = max(height[i], left_max[i-1])

    right_max[len(height)-1] = height[len(height)-1]
    for j in range(len(height)-2, -1, -1):
        right_max[j] = max(height[j], right_max[j+1])

    for k in range(1, len(height)):
        ans += min(left_max[k], right_max[k]) - height[k]
    return ans


print(find_tapping_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


