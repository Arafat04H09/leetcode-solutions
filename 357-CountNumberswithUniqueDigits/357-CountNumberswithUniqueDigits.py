class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        def makeUnique(numDigits):
            if numDigits == 1:
                return 10
            ans = 9
            digitsLeft = numDigits - 1
            numsLeftToPick = 9
            while digitsLeft > 0:
                ans *= numsLeftToPick
                numsLeftToPick -= 1
                digitsLeft -= 1

            return ans + makeUnique(numDigits - 1)
        
        return makeUnique(n)