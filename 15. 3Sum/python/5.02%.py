class Solution(object):
    def threeSum(self, nums):
        output = set()
        total = len(nums)
        hashmap = {nums[i]: i for i in range(total)}
        for i in range(total):
            for j in range(total):
                if nums[i] <= nums[j]:
                    current_sum = nums[i] + nums[j]
                    if nums[j] <= -current_sum:
                        try:
                            k = hashmap[ -current_sum ]
                            if k != i and i != j and j != k:
                                new_element = ( nums[i], nums[j], nums[k] )
                                output.add(new_element)
                        except:
                            pass
            
        return list(output)
