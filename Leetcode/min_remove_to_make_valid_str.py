"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

leetcode 1249


Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"


"""

def minRemoveToMakeValid(s):

    # mark indexes to remove.
    index_to_remove = set()

    # stack for index
    stack = []

    # check indexes for string that is invalid
    for i, c in enumerate(s):
        if c not in "()":
            continue
        if c == "(":
            stack.append(i)
        elif stack != []:
            stack.pop()
        else:
            index_to_remove.add(i)

    index_to_remove = index_to_remove.union(set(stack))

    # now we have all indexes that need to remove
    final_string = []
    for i,c in enumerate(s):
        if i not in index_to_remove:
            final_string.append(c)
    return "".join(final_string)

print(minRemoveToMakeValid("lee(t(c)o)de)"))





