class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        
        maxHeap = []
        current = 0
        
        for _ in range(k):
            while current < len(projects) and projects[current][0] <= w:
                heapq.heappush(maxHeap, -projects[current][1])
                current += 1
            
            if not maxHeap:
                break
            
            w += -heapq.heappop(maxHeap)
        
        return w