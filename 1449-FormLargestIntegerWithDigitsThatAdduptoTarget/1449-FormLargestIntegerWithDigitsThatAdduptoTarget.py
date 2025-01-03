class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = [-1] * (target + 1)
        dp[0] = 0 
        
        for curCost in range(1, target + 1):
            for digit, c in enumerate(cost):
                if curCost >= c and dp[curCost - c] != -1:
                    dp[curCost] = max(dp[curCost], dp[curCost - c] * 10 + (digit + 1))
        
        return str(dp[target]) if dp[target] != -1 else "0"
        