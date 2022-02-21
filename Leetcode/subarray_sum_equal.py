"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
Input: nums = [1,1,1], k = 2
Output: 2
Leetcode:560
"""


def brute_force(nums, k):
    count = 0
    #subarray = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n+1):
            total_sum = 0
            for l in range(i, j):
                total_sum += nums[l]
            if total_sum == k:
                count += 1
                #subarray.append(nums[i:j])
    return count


def brute_force_2(nums, k):
    count = 0
    subarray = []
    n = len(nums)
    for i in range(n):
        total_sum = 0
        for j in range(i, n):
            total_sum += nums[j]
            if total_sum == k:
                subarray.append(nums[i:j+1])
                count += 1
    return count, subarray


def optimal_solution(nums, k):
    count = 0
    n = len(nums)
    total_sum = 0
    d = {}
    d[0] = 1
    for i in range(n):
        total_sum += nums[i]
        if total_sum - k in d.keys():
            count += d.get(total_sum - k)
        d[total_sum] = d.get(total_sum, 0) + 1
    return count

print(optimal_solution([3,4,7,2,-3,1,4,2],7))