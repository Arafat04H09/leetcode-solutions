class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = defaultdict(int)
        n = len(nums)

        for num in nums:
            m[num] += 1

            if m[num] > n//2:
                return num
        
        return -1