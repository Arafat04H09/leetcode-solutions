class Solution(object):
    def rob(self, nums):
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            robbedLastHouse = dp[i - 1]
            didntRobLastHouse = (dp[i - 2] if i - 2 >= 0 else 0) + nums[i - 1]
            
            dp[i] = max(robbedLastHouse, didntRobLastHouse)
        
        return dp[-1]