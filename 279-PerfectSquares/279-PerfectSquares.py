class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("inf")] * (n + 1)
        squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        dp[0] = 0

        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break
                
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]
