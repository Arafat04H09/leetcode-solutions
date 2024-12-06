class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = k * (k + 1) // 2 
        last = 0
        heapq.heapify(nums)
        while nums and nums[0] <= k:
            n = heapq.heappop(nums)  
            if n != last:
                k += 1
                res += k - n
            last = n
        return res

            
