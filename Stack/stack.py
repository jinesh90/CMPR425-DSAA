

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


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print("Now stack length should be: {}\n".format(len(s)))
    assert len(s) == 4
    while not s.is_empty():
        s.pop()
    print("Now stack should be empty and length should be 0\n")
    assert len(s) == 0



