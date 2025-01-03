class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = nums[0]
        right = sum(nums) - left

        ways = 1 if left >= right else 0

        for i in range(1, len(nums) -1):
            left += nums[i]
            right -= nums[i]

            if left >= right:
                ways += 1
        
        return ways