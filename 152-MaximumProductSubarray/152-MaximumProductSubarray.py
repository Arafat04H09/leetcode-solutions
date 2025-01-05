class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dpMax = [0] * len(nums)
        dpMin = [0] * len(nums)
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]

        for i in range(1, len(nums)):
            dpMax[i] = max(dpMax[i - 1] * nums[i], dpMin[i -1] * nums[i], nums[i])
            dpMin[i] = min(dpMax[i - 1] * nums[i], dpMin[i -1] * nums[i], nums[i])
        
        
        return max(max(dpMax), max(dpMin))