class Solution(object):
    def threeSum(self, nums):
        
        total = len(nums)
        ordered = nums
        ordered.sort()
        out = []

        i = 0
        while i < total:

            if i > 0 and ordered[i] == ordered[i - 1]:
                i += 1
                continue

            j, k = i + 1, total - 1
            while j < k:
                if ordered[j] + ordered[k] > -ordered[i]:
                    k -= 1
                elif ordered[j] + ordered[k] < -ordered[i]:
                    j += 1
                else:
                    element = [ ordered[i], ordered[j], ordered[k] ]
                    if element not in out:
                        out.append(element)
                    if j + 1 < k:
                        if ordered[j + 1] + ordered[k] == -ordered[i]:
                            j += 1
                            continue
                        elif ordered[j] + ordered[k - 1] == -ordered[i]:
                            k -= 1
                            continue
                        j += 1
                    else:
                        j += 1
            
            i += 1
            
        return out
                