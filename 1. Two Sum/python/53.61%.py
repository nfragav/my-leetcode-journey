class Solution(object):
    def twoSum(self, nums, target):
        for upper in reversed(range(len(nums))):
            for lower in range(upper):
                if nums[upper] + nums[lower] == target:
                    return lower, upper