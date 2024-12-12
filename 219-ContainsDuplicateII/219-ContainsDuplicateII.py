class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = defaultdict(int)

        for index, num in enumerate(nums):
            if num in m and abs(index - m[num]) <= k: 
                return True
            m[num] = index

        return False
            
        