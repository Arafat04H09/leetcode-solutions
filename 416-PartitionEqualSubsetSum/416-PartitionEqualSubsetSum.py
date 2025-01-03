class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        target = s // 2
        memo = {0}

        for num in nums:
            for possibleSum in list(memo):
                memo.add(possibleSum + num)
        
        return target in memo

