class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-num for num in gifts]
        heapify(nums)
        
        while k:
            tmp = int(math.floor(math.sqrt(-heappop(nums))))
            heappush(nums, -tmp)
            k -= 1
            
        return -sum(nums)
