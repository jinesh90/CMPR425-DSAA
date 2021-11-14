"""
leetcode problem # 3 find longest substring.
"""



# def char_repeat(s, start, end):
#     char_array = [0] * 128
#     for i in range(start, end+1):
#         c = s[i]
#         char_array[ord(c)] += 1
#         if char_array[ord(c)] > 1:
#             return False
#     return True
#
#
# def find_longest_brute_force(s):
#     """
#
#     :param s:
#     :return:
#     """
#     max_len = 0
#     for i in range(len(s)):
#         for j in (i, len(s)):
#             if char_repeat(s, i, j):
#                 max_len = max(max_len, j-i+1)
#     return max_len
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


s = "abcabcbb"
print(find_longest_brute_force(s))
