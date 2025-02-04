class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0 
        s = 0
        m = 0

        for _, num in enumerate(nums):
            if num > prev:
                s += num
            else:
                s = num
            m = max(m, s)
            prev = num
        
        return m