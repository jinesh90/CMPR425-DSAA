"""
leet code problem 42
two pointer method
"""


def find_tapping_water(height):
    ans = 0
    i = 0
    j = len(height) - 1
    left_max = 0
    right_max = 0

    while i < j:
        if height[i] < height[j]:
            if height[i] >= left_max:
                left_max = height[i]
            else:
                ans += left_max - height[i]
            i += 1
        else:
            if height[j] >= right_max:
                right_max = height[j]
            else:
                ans += right_max - height[j]
            j -= 1
    return ans


print(find_tapping_water([4,2,0,3,2,5]))



