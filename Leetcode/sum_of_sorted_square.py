def sum_of_sorted_array(array):
    n = len(array)
    i = 0
    j = n - 1
    k = n - 1
    result = [0] * len(array)
    # for a in range(n):
    #     result[a] = 0
    while j >= i:
        i2 = array[i] * array[i]
        j2 = array[j] * array[j]
        if i2 >= j2:
            result[k] = i2
            i = i + 1
        else:
            result[k] = j2
            j = j - 1
        k = k - 1
    assert k == -1

    return result

a = [-4,-2,0,1,4,10]

print (sum_of_sorted_array(a))