class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        gcd_, ans = gcd(a,b), 1

        for n in range(1, gcd_//2 +1):

            if gcd_%n == 0:
 
                ans+= 1

        return ans
