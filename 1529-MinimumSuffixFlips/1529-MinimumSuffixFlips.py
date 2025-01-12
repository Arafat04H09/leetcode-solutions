class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        boolean = '0'
        flips = 0

        for i in range(len(target)):
            if target[i] != boolean:
                boolean = '1' if boolean == '0' else '0'
                flips += 1

        return flips