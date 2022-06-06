"""
check basic valid palindrome
"""

def valid_palindrome_1(s):
    return s == s[::-1]



def valid_palindrome_2(s):
    """
    two pointers approch.
    :param s:
    :return:
    """
    n = len(s)
    i = 0
    j = n - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def valid_palindrome_3(s):
    """
    leetcode 680
    :param s:
    :return:
    """
    def is_valid(s,i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            # check both possiblity by omitting a single word
            return is_valid(s, i+1, j) or is_valid(s, i, j-1)
        i += 1
        j -= 1
    return True

# print(valid_palindrome_1("wabbaw"))
# print(valid_palindrome_2("wabbaw"))
print(valid_palindrome_3("wabbaw"))