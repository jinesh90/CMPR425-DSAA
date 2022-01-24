"""
hop easy and hop function. find hops to get target for example
find steps to go target 5 in a[2,3,5,1,4,0]
"""

def _hop_easy(array,target):
    hops = 0
    t = target
    while(True):
        if (array[t] == target):
            return hops
        else:
            t = array[t]
            hops += 1
    return hops

def _hop_easy_2(array,target):
    hops = 0
    t = target
    while(array[t] != target):
        t = array[t]
        hops += 1
    return hops


a = [3,2,5,1,4,0]
print(_hop_easy_2(a, 5))

