class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = Counter(nums)

        for num in c.values():
            if num % 2 != 0:
                return False
        
        return True