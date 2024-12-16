class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        nums = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums)

        while k > 0:
            num, index = heapq.heappop(nums)

            heapq.heappush(nums, (num * multiplier, index))
            k -= 1
        
        ans = [0] * len(nums)

        for num,i in nums:
            ans[i] = num
        
        return ans