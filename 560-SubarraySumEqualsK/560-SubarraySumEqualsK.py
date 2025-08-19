# Last updated: 8/19/2025, 12:44:49 AM
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        waysToReach = defaultdict(int)
        waysToReach[0] = 1
        running = 0
        ans = 0

        for num in nums:
            running += num
            ans += waysToReach[running - k]
            waysToReach[running] += 1
        
        return ans