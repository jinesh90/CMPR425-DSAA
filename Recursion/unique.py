"""
find unique element from an array.
abuse recursion.
"""
global st


def unique(s,start,stop, st):
    # base case
    st = 0
    if stop - start <= 1:
        return True
    elif not unique(s, start, stop-1, st+1):
        return False
    elif not unique(s, start+1, stop, st+1):
        return False
    else:
        return s[start] != s[stop-1]

print(unique([1,2,3,4],0,3,0))
