class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        l, r = 0, len(nums) - 1

        while l < r:
            s += int(str(nums[l]) + str(nums[r]))
            l += 1
            r-= 1

        if l == r:
            s += nums[l]
        
        return s
        