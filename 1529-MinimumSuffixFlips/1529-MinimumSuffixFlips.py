class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        boolean = '0' #represents 0, True = 1
        flips = 0 #number of flips

        for _, num in enumerate(target):
            if num != boolean: 
                flips += 1
                boolean = '0' if num == '0' else '1'
        
        return flips


