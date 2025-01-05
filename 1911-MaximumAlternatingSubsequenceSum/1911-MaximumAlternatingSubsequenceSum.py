class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * 2

        for i in range(len(nums)):
            n1 = max(dp[1] + nums[i], dp[0])
            n2 = max(dp[0] - nums[i], dp[1])

            dp = [n1, n2]
        
        return dp[0]
