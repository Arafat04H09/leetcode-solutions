class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = -100001
        m = -100001

        for _, num in enumerate(nums):
            cur = max(cur + num, num)
            m = max(cur, m)
        
        return m