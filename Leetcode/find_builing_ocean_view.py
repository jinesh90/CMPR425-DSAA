"""
Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

"""


def building_with_ocean_view(heights):
    # populate right max array

    ocean_view = []
    n = len(heights)
    right_max = [0] * n
    right_max[n-1] = heights[n - 1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(heights[i], right_max[i+1])

    # now right most build always have ocen view
    ocean_view.append(n-1)

    for i in range(n-2, -1, -1):
        if heights[i] >= right_max[i]:
            ocean_view.append(i)

    ocean_view.reverse()
    return ocean_view

print(building_with_ocean_view([4, 5, 8, 1]))
