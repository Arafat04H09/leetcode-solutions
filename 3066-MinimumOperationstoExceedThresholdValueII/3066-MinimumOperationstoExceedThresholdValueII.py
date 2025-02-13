class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        steps = 0
        heapq.heapify(nums)  

        while len(nums) > 1 and nums[0] < k:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)

            heapq.heappush(nums, min(first, second) * 2 + max(first, second))
            steps += 1

        return steps