"""
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.
Input: s = "owoztneoer"
Output: "012"

"""

from collections import Counter

def get_digit(s):

    out = {}
    count = Counter(s)
    print(count)

    out["0"] = count["z"]
    out["2"] = count["w"]
    out["4"] = count["u"]
    out["6"] = count["x"]
    out["8"] = count["g"]
    out["3"] = count['h'] - out['8']
    out["5"] = count["f"] - out["4"]
    out["7"] = count["s"] - out["6"]
    out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
    out["1"] = count["n"] - out["7"] - 2 * out["9"]
    print(out)
    output = [key * out[key] for key in sorted(out.keys())]
    return "".join(output)


print(get_digit("owoztneoer"))