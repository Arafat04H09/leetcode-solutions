class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        freq = Counter(arr)
        
        heap = list(freq.values())
        heapq.heapify(heap)
        
        while k > 0 and heap:
            smallest = heapq.heappop(heap)
            if k >= smallest:
                k -= smallest
            else:
                heapq.heappush(heap, smallest - k)
                k = 0
        
        return len(heap)

