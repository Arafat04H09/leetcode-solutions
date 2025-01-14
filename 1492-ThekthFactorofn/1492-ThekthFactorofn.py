class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factorNum = 0

        for i in range(1, n//2 + 1):
            if n % i == 0:
                factorNum += 1
            
            if factorNum == k:
                return i 
        
        return n if factorNum == k - 1 else -1