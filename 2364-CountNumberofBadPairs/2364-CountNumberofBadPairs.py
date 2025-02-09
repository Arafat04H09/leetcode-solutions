class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        badPairs = 0
        m = defaultdict(int)

        for index, num in enumerate(nums):
           badPairs += index - (m[num - index])
           m[num - index] += 1
        
        return badPairs
        