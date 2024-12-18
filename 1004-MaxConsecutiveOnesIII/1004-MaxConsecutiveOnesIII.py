class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        maxLen = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                k -= 1

            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1

            maxLen = max(maxLen, end - start + 1)
        
        return maxLen
