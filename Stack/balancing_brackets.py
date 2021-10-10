from Coding.stack.stack import Stack


def is_matched(ch1, ch2):
    if ch1 == "{" and ch2 == "}":
        return True
    elif ch1 == "(" and ch2 == ")":
        return True
    elif ch1 == "[" and ch2 == "]":
        return True
    else:
        return False


def is_balanced_string(string):
    string_index = 0
    is_balanced = True
    s = Stack()
    while string_index != len(string) and is_balanced:
        if string[string_index] in "[{(":
            s.push(string[string_index])
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_matched(top,string[string_index]):
                    is_balanced  = False
        string_index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False





print("String : (((({}))))] Balanced or not?")
print(is_balanced_string("(((({}))))"))






