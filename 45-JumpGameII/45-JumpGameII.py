class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        jumps  = 0
        curEnd = 0
        curFarthest = 0

        for i in range(len(nums)):
            curFarthest = max(curFarthest, i + nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = curFarthest

                if curEnd >= len(nums) - 1:
                    break
        
        return jumps



