class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {n: i for i,n in enumerate(nums)}
        for n,i in hashmap.items():
            try:
                if hashmap[target - n] != i:
                    return [i, hashmap[target - n]]
            except:
                pass

        return [i for i in range(len(nums)) if nums[i] == target / 2]