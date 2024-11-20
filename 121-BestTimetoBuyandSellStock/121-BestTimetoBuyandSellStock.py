class Solution(object):
    def maxProfit(self, prices):
        minValue = 10001
        maxProfit = 0

        for price in prices:
            if price < minValue:
                minValue = price
                continue 
            maxProfit = max(maxProfit, price - minValue)
        
        return maxProfit