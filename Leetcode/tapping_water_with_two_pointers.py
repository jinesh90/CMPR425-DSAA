"""
leet code problem 42
two pointer method
"""


def find_tapping_water(a):
    ans = 0
    i = 0
    j = len(a) - 1
    left_max = 0
    right_max = 0

    while i < j:
        if a[i] < a[j]:
            if a[i] >= left_max:
                left_max = a[i]
            else:
                ans += left_max - a[i]
            i += 1
        else:
            if a[j] >= right_max:
                right_max = a[j]
            else:
                ans += right_max - a[j]
            j -= 1
    return ans


print(find_tapping_water([4,2,0,3,2,5]))



