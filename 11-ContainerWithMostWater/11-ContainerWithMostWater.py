class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        l, r = 0, len(height) - 1

        while l < r:
            maxWater = max(min(height[l], height[r]) * (r - l), maxWater)

            if height[l] > height[r]:
                r-= 1
            else:
                l+= 1
        
        return maxWater