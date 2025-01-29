class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        
        first, second = 1, 2

        for i in range(2, n):
            first, second = second, first + second

        return second
        
        
        