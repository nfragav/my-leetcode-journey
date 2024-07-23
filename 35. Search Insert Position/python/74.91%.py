class Solution(object):
    def binSearch(self, nums, lower, upper, target):
        i = (lower + upper) // 2
        if upper == lower:
            if nums[i] < target:
                return i + 1
            elif nums[i] > target:
                return i

        if nums[i] < target:
            return self.binSearch(nums, min(upper, i + 1), upper, target)
        elif nums[i] > target:
            return self.binSearch(nums, lower, max(0, i - 1), target)
        return i

    def searchInsert(self, nums, target):
        return self.binSearch(nums, 0, len(nums) - 1, target)
