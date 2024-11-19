class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort() 
        l, r = 0, len(nums) - 1
        c = 0

        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                c+= 1
                l+= 1
                r-= 1
            elif s > k:
                r -= 1
            else:
                l += 1
        
        return c