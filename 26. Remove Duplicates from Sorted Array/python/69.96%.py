class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = [nums[i] for i in range(len(nums)) if i == 0 or (i > 0 and nums[i - 1] != nums[i])]
        return len(nums)
