class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = AND = start = 0
        for end in range(len(nums)):
            while AND & nums[end]:
                AND ^= nums[start]
                start += 1

            AND |= nums[end]
            res = max(res, end - start  + 1)
        
        return res
        