"""
leetcode problem # 3 find longest substring.
using two pointers and hash
"""

def longest_substring(s):
    m = dict()
    result = 0
    i = 0
    n = len(s)
    substrings = []
    for j in range(n):
        if s[j] in m:
            i = max(m[s[j]], i)
        result = max(result, j - i + 1)
        substrings.append(s[i:j+1])
        m[s[j]] = j + 1
    print(substrings)
    return result


s = "abcabcbbafghai"
print(longest_substring(s))
