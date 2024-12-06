class Solution(object):
    def maxProfit(self, prices):
        m = 10001
        maxProfit = 0

        for price in prices:
            if price < m:
                m = price
                continue
            maxProfit = max(maxProfit, price -m)
        
        return maxProfit