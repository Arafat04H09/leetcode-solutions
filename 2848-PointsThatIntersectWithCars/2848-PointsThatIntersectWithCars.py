class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        line = [0] * 102

        for start, end in nums:
            line[start] += 1
            line[end + 1] -= 1
        
        p = 0
        c = 0

        for i in range(102):
            c += line[i]

            if c > 0:
                p += 1
        
        return p