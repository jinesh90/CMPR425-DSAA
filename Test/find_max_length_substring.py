

def find_max_substring(strs):
    # dict for index tracking of char
    m = dict()

    # substring folders
    sub_strs = []

    # first pointer
    i = 0

    # total length
    n = len(strs)
    max_length = 0

    # second pointer for iterator
    for j in range(n):
        # check j in dict
        if strs[j] in m:
            # in case of char in dict, adjust first pointer
            i = max(m[strs[j]], i)

        # get max substring
        sub_strs.append(strs[i:j+1])

        # track max length
        max_length = max(max_length, j-i+1)
        # append char in dict
        m[strs[j]] = j + 1
    print((sub_strs))
    return max_length


s = "abcabcbbafghaioa"
print(find_max_substring(s))