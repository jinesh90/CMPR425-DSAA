"""
print("String : (((({}))))] Balanced or not?")
print(is_balanced_string("(((({}))))]"))


print("String : {1+[2*(3/4)-1]+2} Balanced or not?")
print(is_balanced_string("{1+[2*(3/4)-1]+2}"))
"""


class Stack:

    def __init__(self):
        self._data = []

    def is_empty(self):
        return self._data == []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self.is_empty():
            return self._data.pop()
        else:
            raise ValueError('Empty stack')

    def top(self):
        if not self.is_empty():
            return self._data[len(self._data)-1]
        else:
            return None

    def __len__(self):
        return len(self._data)


def is_balanced_string(st):
    s = Stack()
    left_str = "({["
    right_str = ")}]"

    for i in st:
        if i in left_str:
            s.push(i)
        elif i in right_str:
            if s.is_empty():
                return False
            else:
                r = s.pop()
                if left_str.index(r) != right_str.index(i):
                    return False
    return s.is_empty()
