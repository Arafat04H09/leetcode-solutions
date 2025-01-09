class Solution(object):
    def maxProfit(self, prices):
        minimum = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minimum)

            minimum = min(minimum, prices[i])

        return maxProfit

