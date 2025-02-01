class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            a = abs(num)

            if nums[a] < 0:
                return a
            nums[a] = -nums[a]
        
        return l