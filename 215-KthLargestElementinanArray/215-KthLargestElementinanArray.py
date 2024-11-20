class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heappushpop(heap, nums[i])
        
        return heap[0]