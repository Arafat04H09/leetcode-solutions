class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        minLen = float("inf")
        start = 0
        curSum = 0

        for end in range(0, len(nums)):
            curSum += nums[end]
            
            while curSum >= target:
                minLen = min(minLen, end - start + 1)
                curSum -= nums[start]
                start += 1

        return minLen if minLen != float("inf") else 0
