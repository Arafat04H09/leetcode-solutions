class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cur = 1
        start = 0
        ways = 0

        for end in range(len(nums)):
            cur *= nums[end]

            while start <= end and cur >= k:
                cur /= nums[start]
                start += 1
            
            if cur < k:
                ways += (end - start + 1)

        return ways

        