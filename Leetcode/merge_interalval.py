"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""


def merge_interval(intervals):
    merged = []
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    for i in intervals:

        # case when not overlapping and empty merger interval
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            # case where overlapping array
            merged[-1][1] = max(merged[-1][1], i[1])

    return merged

print(merge_interval([[1,3], [2,6], [8,10], [15,18]]))