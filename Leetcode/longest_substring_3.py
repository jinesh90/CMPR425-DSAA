"""
leetcode problem # 3 find longest substring.
"""

def check(substring):
    d = {}
    for c in substring:
        if c in d.keys():
            return False
        else:
            d[c] = 1
    return True


def find_longest_substring(s):
    max_len = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if check(s[i:j+1]):
                max_len = max(max_len, j-i+1)
    return max_len


s = "abcabcbbafghai"
print(find_longest_substring(s))