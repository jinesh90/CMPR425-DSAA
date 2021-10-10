"""
reverse list by using recursion
"""

def reverse_list(array,start,stop):
    if start < stop -1:
        array[start], array[stop-1] = array[stop-1], array[start]
        reverse_list(array,start+1,stop-1)



a = [1,2,3,4,5]
reverse_list(a, 0, 5)
print(a)
