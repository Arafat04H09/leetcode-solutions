class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, sum(candies) / k
        while left < right:
            mid = (left + right + 1) / 2
            if k > sum(candy / mid for candy in candies):
                right = mid - 1
            else:
                left = mid
        return left