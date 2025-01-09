class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = -float("inf")
        c = 0

        for num in nums:
            c = max(c + num, num)
            m = max(m, c)
    
        return m