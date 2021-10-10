from stack import Stack


def reversing_string(st):
    s = Stack()
    reverse_str = ""
    for i in st:
        s.push(i)
    while not s.is_empty():
        reverse_str += s.pop()
    return reverse_str


if __name__ == '__main__':
    str1 = ""
    str2 = "j"
    str3 = "ji"
    str4 = "jinesh"
    print(reversing_string(str1))
    print(reversing_string(str2))
    print(reversing_string(str3))
    print(reversing_string(str4))



