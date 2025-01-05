class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dpMax = [-float("inf")] * n
        dpMin = [float("inf")] * n

        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        for i in range(1, n):
            dpMax[i] = max(dpMax[i - 1] + nums[i], nums[i])  
            dpMin[i] = min(dpMin[i - 1] + nums[i], nums[i])
        
        if max(dpMax) < 0:
            return max(dpMax)
        
        return max(max(dpMax), sum(nums) - min(dpMin))
