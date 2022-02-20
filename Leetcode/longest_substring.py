"""
leetcode problem # 3 find longest substring.
"""


def find_longest_brute_force(s):
    def check(start, end):
        chars = [0] * 128
        for i in range(start, end + 1):
            c = s[i]
            chars[ord(c)] += 1
            if chars[ord(c)] > 1:
                return False
        return True
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i, n):
            if check(i, j):
                res = max(res, j - i + 1)
    return res


s = "abcabcbbafghai"
print(find_longest_brute_force(s) == 5)
