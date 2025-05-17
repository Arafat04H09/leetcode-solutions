# Last updated: 5/17/2025, 3:59:58 PM
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros, twos = 0, len(nums) - 1
        cur = 0

        while cur <= twos:
            if nums[cur] == 0:
                nums[zeros], nums[cur] = nums[cur], nums[zeros]
                zeros += 1
            elif nums[cur] == 2:
                nums[twos], nums[cur] = nums[cur], nums[twos]
                twos -= 1
                cur -= 1
            cur += 1
        
        return nums