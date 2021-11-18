"""
leetcode # 341
flattern list to a single list
"""

final_array = []

def flattern_list(nestedList):

    for obj in nestedList:
        if isinstance(obj, int):
            final_array.append(obj)
        else:
            flattern_list(obj)

flattern_list([[1,1],2,[3],[1,2,3],[],4,5,[6,[7,[8,[9]]]]])
print(final_array)


