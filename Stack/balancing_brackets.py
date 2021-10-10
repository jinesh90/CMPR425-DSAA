from stack import Stack


def is_balanced_string(st):
    """
    check string is balanced or not
    :param st:
    :return: boolean
    """
    left_param = "({["
    right_params = ")}]"

    s = Stack()

    for c in st:
        if c in left_param:
            s.push(c)
        elif c in right_params:
            if s.is_empty():
                return False
            rc = s.pop()
            if left_param.index(rc) != right_params.index(c):
                return False
    return s.is_empty()


print("String : (((({}))))] Balanced or not?")
print(is_balanced_string("(((({}))))]"))


print("String : {1+[2*(3/4)-1]+2} Balanced or not?")
print(is_balanced_string("{1+[2*(3/4)-1]+2}"))





