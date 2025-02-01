class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(1,len(nums)):
            if (nums[i] + nums[i - 1]) % 2 != 1:
                return False
        
        return True