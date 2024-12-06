class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        canJumpTo = nums[0]

        for i in range(1, len(nums)):
            if i > canJumpTo:
                return False
            
            canJumpTo = max(canJumpTo, i + nums[i])
        
        return canJumpTo >= len(nums) - 1