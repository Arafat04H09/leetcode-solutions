class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numIndex = 0

        for index in range(1, len(nums)):
            if nums[index] != nums[numIndex]:
                numIndex += 1
                nums[numIndex] = nums[index]
        
        return numIndex + 1
            
