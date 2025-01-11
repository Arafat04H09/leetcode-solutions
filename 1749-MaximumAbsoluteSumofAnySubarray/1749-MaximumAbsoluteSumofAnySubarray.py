class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = 0
        maximum = 0
        curMax = 0
        curMin = 0

        for i in range(len(nums)):
            curMax = max(curMax + nums[i], nums[i])
            curMin = min(curMin + nums[i], nums[i])
            
            minimum = min(minimum, curMin)
            maximum = max(maximum, curMax)
        
        return max(abs(minimum), maximum)