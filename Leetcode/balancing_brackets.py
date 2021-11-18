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
    left_param = "({["
    right_params = ")}]"

    s = Stack()
    for i in st:
        if i in left_param:
            s.push(i)
        elif i in right_params:
            if s.is_empty():
                return False
            a = s.pop()
            if right_params.index(i) != left_param.index(a):
                return False
    return s.is_empty()