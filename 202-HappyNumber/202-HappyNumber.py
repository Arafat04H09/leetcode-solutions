class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memo = set()

        while n != 1:
            if n in memo:
                return False  
            
            memo.add(n)
            temp = 0

            while n > 0:
                digit = n % 10
                temp += digit ** 2
                n //= 10
            
            n = temp

        return True

                      
                 