"""
leet code problem 42
brute force method
"""

def find_tapping_water(a):
    ans = 0
    for i in range(0, len(a)):
        left_max = 0
        right_max = 0
        for j in range(i, -1, -1):
            left_max = max(left_max, a[j])
        for j in range(i, len(a)):
            right_max = max(right_max, a[j])
        ans += min(left_max, right_max) - a[i]
    return ans


print(find_tapping_water([4,2,0,3,2,5]))



