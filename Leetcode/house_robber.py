"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

"""


def house_robber(nums):
    n = len(nums)

    if n == 0:
        return
    if n == 1 or n == 2:
        return max(nums)
    else:
        total_robbery = [0] * n
        # assign first robbery
        total_robbery[0] = nums[0]
        total_robbery[1] = nums[1]

        # now fill data dynamically
        for i in range(1, n):
            total_robbery[i] = max(total_robbery[i-1], nums[i] + total_robbery[i-2])

        return total_robbery[-1]



house_robber([2,7,9,3,1])
