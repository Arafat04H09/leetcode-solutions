class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        c = 0
        prev = float("inf")

        for num in nums: #decreasing 
            if num < prev:
                c += 1
                m = max(c, m)
            else:
                c = 1
            prev = num
        
        c = 0
        prev = -float("inf")
        for num in nums:
            if num > prev:
                c += 1
                m = max(c, m)
            else:
                c = 1
            prev = num

        return m