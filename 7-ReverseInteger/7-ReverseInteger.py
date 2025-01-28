class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        ans = 0
        
        while x > 0:
            ans = ans * 10 + x % 10
            x //= 10
        
        return ans * sign if -2 ** 31 < ans < 2**31 else 0

        
        