class Solution(object):
    def maxArea(self, height):
        total = len(height)
        max_area = 0
        i, j = 0, total - 1
        while i < j:
            max_area = max(min(height[i], height[j]) * (j - i), max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
            
