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
        result = nums[0]

        for idx in range(1, n):
            num = nums[idx]
            dpMax[idx] = max(dpMax[idx - 1] * num, dpMin[idx - 1] * num, num)
            dpMin[idx] = min(dpMin[idx - 1] * num, dpMax[idx - 1] * num, num)

            result = max(result, dpMax[idx])

        return result