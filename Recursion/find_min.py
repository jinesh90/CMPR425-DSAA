

def find_min(array, i):
    if i == len(array) - 1:
        return array[i]
    else:
        tmp_min = array[i]
        i = i + 1
        min_frm = find_min(array, i)
        return min(tmp_min, min_frm)

a = [2, 1, 3, 10, 53, 23, -1, 2, 5, 0, 34, 8]
#a = [x for x in range(1000)]
print (find_min(a, 0))



