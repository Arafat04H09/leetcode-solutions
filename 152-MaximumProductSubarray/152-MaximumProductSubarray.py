class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1 and nums[0] < 0:
            return nums[0]
            
        dpMax = [0] * n
        dpMin = [0] * n

        for idx, num in enumerate(nums):
            dpMax[idx] = max(dpMax[max(0, idx - 1)] * num, dpMin[max(0, idx -1)] * num, num)
            dpMin[idx] = min(dpMin[max(0, idx - 1)] * num, dpMax[max(0, idx -1)] * num, num)
        
        return max(max(dpMax), max(dpMin))