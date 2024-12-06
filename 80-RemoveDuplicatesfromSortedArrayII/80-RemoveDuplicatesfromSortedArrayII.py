class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)
        currentNum = None
        count = 0
        i = 0

        while i < len(nums):
            if nums[i] == currentNum:
                count += 1
                if count > 2:
                    nums.pop(i)
                    k -= 1
                else:
                    i += 1
            else:
                currentNum = nums[i]
                count = 1
                i += 1

        return 
