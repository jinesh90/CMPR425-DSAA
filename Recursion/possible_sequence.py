"""
permutation of string by recursion
"""


def swap(array, i, j):
    """
    swap routine for array swap
    :param array:
    :param i:
    :param j:
    :return:
    """
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

vone = []

def permutation(array, current_pointer=0):
    # define another pointer end pointer that end of seq
    end_pointer = len(array) - 1

    # base case
    if current_pointer == end_pointer:
        vone.append(" ".join(array))
        #(array)

    # second case
    for i in range(current_pointer, end_pointer + 1):
        swap(array, current_pointer, i)
        permutation(array, current_pointer+1)
        swap(array, current_pointer, i)

print(permutation(["a","b","c","d"]))
print(len(vone))