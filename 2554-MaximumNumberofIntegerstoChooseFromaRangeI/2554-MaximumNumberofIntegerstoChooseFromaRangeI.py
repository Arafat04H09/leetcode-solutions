class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        c = 0
        curSum = 0

        s = set(banned)

        for i in range(1, n + 1):
            if i in s:
                continue 
            if curSum + i <= maxSum:
                curSum += i
                c += 1
            else:
                break

        return c
            