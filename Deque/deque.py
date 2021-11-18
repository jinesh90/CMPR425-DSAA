"""
create deque where operations are below
d = Deque()
d.append(1) ---> append right @ O(1)
d.pop() ---> pop right @ O(1)
d.appendleft(1) --> append left @ O(1)
d.popleft() ---> pop left @ O(1)
len(d) --> give total element in deque @ O(1)
print(d) ---> print dequeue

We will use two dynamic array approach.
"""


class Dequeue:

    def __init__(self):
        # left array
        self._la = []
        # right array
        self._ra = []

        # we can not use 0th position from both array
        self._la.append(-9999999999)
        self._ra.append(9999999999)

        # pointers for track l array and r array

        self._l = 0
        self._r = 0

    def is_empty(self):
        return self._r == 0 and self._l == 0

    def append(self, v):
        self._r = self._r + 1
        if self._r == 0:
            self._r = 1
        l = len(self._ra)
        if self._r < l:
            self._ra[self._r] = v
        else:
            self._ra.append(v)

    def appendleft(self, v):
        self._l = self._l - 1
        if self._l == 0:
            self._l = -1
        left_array_len = len(self._la)
        if self._l > left_array_len:
            self._la[self._l] = v
        else:
            self._la.append(v)







d = Dequeue()
print(d.is_empty())



