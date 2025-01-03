class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()
        dp = [1] * len(pairs)
        maxLength = 1

        for i in range(1, len(pairs)):
            for j in range(0, i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = dp[j] + 1
                maxLength = max(maxLength, dp[i])

        return maxLength