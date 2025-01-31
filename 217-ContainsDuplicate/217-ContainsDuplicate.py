class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = Counter(nums)

        for freq in c.values():
            if freq > 1:
                return True
        
        return False