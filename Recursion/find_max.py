def find_max(array, i):
    if i == len(array) - 1:
        return array[i]
    else:
        tmp_min = array[i]
        i = i + 1
        min_frm = find_max(array, i)
        if tmp_min > min_frm:
            return tmp_min
        else:
            return min_frm
        #return max(tmp_min, min_frm)

#a = [x for x in range(1000)]
a = [2, 1, 3, 10,60, 54, -1, 2, 5, 0, 34, 8]
print (find_max(a, 0))