class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = defaultdict(int)

        for num in nums:
            m[num] += 1
            if m[num] > 1:
                return num
        
        return -1