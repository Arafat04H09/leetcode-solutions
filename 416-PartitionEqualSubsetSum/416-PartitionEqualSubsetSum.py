class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)
        if target % 2 != 0:
            return False

        target //= 2
        dp = [False] * (target + 1)
        dp[0] = True 

        for num in nums:
            for j in range(target, num - 1, -1): 
                dp[j] = dp[j] or dp[j - num]

        return dp[target]

