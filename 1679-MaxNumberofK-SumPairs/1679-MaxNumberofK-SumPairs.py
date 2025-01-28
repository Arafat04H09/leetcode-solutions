class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        pops = 0
        left, right = 0, len(nums) - 1

        while left < right:
            s = nums[left] + nums[right]

            if s == k:
                pops += 1
                left += 1
                right -= 1
            elif s > k:
                right -= 1
            else:
                left += 1
    
        return pops
