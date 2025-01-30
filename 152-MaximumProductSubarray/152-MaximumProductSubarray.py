class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dpMax = [0] * n
        dpMin = [0] * n

        dpMax[0] = dpMin[0] = nums[0]

        for idx in range(1, n):
            dpMax[idx] = max(dpMax[idx - 1] * nums[idx], dpMin[idx - 1] * nums[idx], nums[idx])
            dpMin[idx] = min(dpMin[idx - 1] * nums[idx], dpMax[idx - 1] * nums[idx], nums[idx])

        return max(dpMax)