import ctypes


class DynamicList(object):
    def __init__(self):
        # initial pointer
        self._k = 0

        # initial list size
        self._capacity = 8

        # initial list memory allocation
        self._a = self._allocate(self._capacity)

    # append operation
    def append(self, item):
        """
        append method like list
        :param item:
        :return:
        """
        if self._capacity > self._k:
            self._a[self._k] = item
        else:
            self._grow()
            self._a[self._k] = item
        self._k += 1

    def find(self, item):
        """
        find method for (linear search).
        :param item:
        :return: int
        """
        for k in range(self._k):
            if self._a[k] == item:
                return k
        return -1

    def delete(self, item):
        """
        delete item if there, O(N) and space capacity O(1)
        :param item:
        :return:
        """
        n = len(self)
        k = 0
        for i in range(n):
            vi = self[i]
            if vi != item:
                assert (k <= i)
                self[k] = vi
                k = k + 1
        self._k = k

    def _allocate(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def _grow(self):
        """
        special module that grow array dynamically.
        :return:
        """
        # inital capacity 8.
        initial_capacity = self._capacity

        # grown capacity 2* os
        new_capacity = initial_capacity * 2
        print("Grow from", initial_capacity, "to", new_capacity, ". This is not O(1)")

        # create new list
        b = self._allocate(new_capacity)

        # copy old list to new list
        for k in range(initial_capacity):
            b[k] = self._a[k]

        # point old list to new one.
        self._a = b

        # change initial capacity.
        self._capacity = new_capacity

    def __len__(self):
        """
        length for list
        :return:
        """
        return self._k

    def __str__(self):
        """
        print list
        :return:
        """
        lst_str = "["
        for k in range(self._k):
            item = self._a[k]
            lst_str += str(item) + ","
        lst_str = lst_str[:-1]
        lst_str += "]"
        return lst_str

    def __setitem__(self, key, value):
        self._a[key] = value

    def __getitem__(self, item):
        return self._a[item]



#
# if __name__ == '__main__':
#     l = DynamicList()
#     l.append(1)
#     l.append(5)
#     l.append(6)
#     l.append(12)
#     l.append(5)
#     l.append(17)
#     l.append(25)
#     l.append(34)
#     l.append(45)
#     l.delete(5)
#     print(len(l))
#     print(str(l))
#     print(l.find(12))
#     print(l.find(5))
#

