import random
from List import DynamicList


class List_grow_and_append:
    def __init__(self):
        self.test_init()

    def test_init(self):
        print("===============Testing grow,append, change an find============")
        d = DynamicList()
        # python list
        l = []
        n = 100
        for i in range(n):
            l.append(i*100)
            d.append(i*100)
        print("size of python list=", len(l))
        print("size of dynamic list=", len(d))
        assert (d[34] == l[34])


class List_delete:
    def __init__(self):
        self.test_init()

    def test_init(self):
        print("=====================Testing delete====================")
        d = DynamicList()
        # python list
        l = []
        n = 100
        for i in range(n):
            l.append(i*100)
            d.append(i*100)
        print("size of python list=", len(l))
        print("size of dynamic list=",len(d))
        assert (d[34] == l[34])

        # delete random element

        random_index = random.randint(1, 50)
        delete_item = random_index * 100

        l.remove(delete_item)
        d.delete(delete_item)
        print(random_index)
        assert (d[random_index] == l[random_index])


if __name__ == '__main__':
    test_1 = List_grow_and_append()
    test_1.test_init()
    test_2 = List_delete()
    test_2.test_init()



