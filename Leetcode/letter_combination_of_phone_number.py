"""
leetcode 17. return letter combination of phone number.
"""


def letter_of_combination(digits):
    """
    brute force approach, because we have constrain 0<=digit<=4, we can use this method.
    :param digits:
    :return:
    """
    phone_map = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4":["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]
    }
    combinations = []
    digit_len = len(digits)
    if digit_len == 0:
        return combinations
    elif digit_len == 1:
        letter_map = phone_map.get(digits)
        return letter_map
    elif digit_len == 2:
        letter_map_1 = phone_map.get(digits[0])
        letter_map_2 = phone_map.get(digits[1])
        combinations = ["{}{}".format(x, y) for x in letter_map_1 for y in letter_map_2]
        return combinations
    elif digit_len == 3:
        letter_map_1 = phone_map.get(digits[0])
        letter_map_2 = phone_map.get(digits[1])
        letter_map_3 = phone_map.get(digits[2])
        combinations = ["{}{}{}".format(x, y, z) for x in letter_map_1 for y in letter_map_2 for z in letter_map_3]
        return combinations
    else:
        letter_map_1 = phone_map.get(digits[0])
        letter_map_2 = phone_map.get(digits[1])
        letter_map_3 = phone_map.get(digits[2])
        letter_map_4 = phone_map.get(digits[3])
        combinations = ["{}{}{}{}".format(x, y, z, q) for x in letter_map_1 for y in letter_map_2 for z in letter_map_3 for q in letter_map_4]
        return combinations



def letter_of_combinamtion_backtrace(digits):
    pass




