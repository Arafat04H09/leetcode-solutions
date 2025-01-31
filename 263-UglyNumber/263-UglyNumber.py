class Solution(object):
    def isUgly(self, n):
        if n < 1:
            return False
        
        while n % 60 == 0:
            n /= 60 
        while n % 15 == 0:
            n /= 15
        while n % 10 == 0:
            n /= 10
        while n % 6 == 0:
            n /= 6
        while n % 5 == 0:
            n /= 5
        while n % 3 == 0:
            n /= 3
        while n % 2 == 0:
            n /= 2
        
        return n == 1