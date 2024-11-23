class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap = []
        
        for i in range(k):
            heapq.heappush(heap, (-abs(arr[i] - x), -arr[i]))
        
        for i in range(k, len(arr)):
            diff = abs(arr[i] - x)
            if diff < -heap[0][0] or (diff == -heap[0][0] and arr[i] < -heap[0][1]):
                heapq.heappushpop(heap, (-diff, -arr[i]))
        
        result = sorted(-num for _, num in heap)
        return result

