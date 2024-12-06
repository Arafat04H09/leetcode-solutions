class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        for i in range(n):
            if abs(nums[i]) > n:
                continue
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1