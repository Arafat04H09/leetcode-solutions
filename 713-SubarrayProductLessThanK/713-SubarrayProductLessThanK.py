class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0

        count = 0
        curProduct = 1
        start = 0

        for end in range(len(nums)):
            curProduct *= nums[end]

            while curProduct >= k and start <= end:
                curProduct /= nums[start]
                start += 1

            count += end - start + 1
        return count

        