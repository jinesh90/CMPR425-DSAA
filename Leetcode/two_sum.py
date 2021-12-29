"""
find the two sum for given target Leetcode 1
"""


def two_sum(nums, target):
    """

    :param nums:
    :param target:
    :return:
    """
    result = {}
    n = len(nums)
    for i in range(n):
        difference = target - nums[i]
        if difference in result:
            return [i, result[difference]]
        result[nums[i]] = i


print(two_sum([8,7,11,15],19))
