"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23

"""

def find_max_subarray(nums):
    current_sub = max_sub = nums[0]

    for i in nums[1:]:
        current_sub = max(i, current_sub + i)
        max_sub = max(max_sub, current_sub)

    return max_sub

a = [-2,1,-3,4,-1,2,1,-5,4]
print(find_max_subarray(a))

