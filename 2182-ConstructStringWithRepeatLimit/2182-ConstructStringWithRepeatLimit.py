class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        counter = Counter(s)
        
        maxHeap = [(-ord(ch), freq) for ch, freq in counter.items()]
        heapq.heapify(maxHeap)
        
        result = []  
        
        while maxHeap:
            ord1, freq1 = heapq.heappop(maxHeap)
            ch1 = chr(-ord1)
            
            addCount = min(freq1, repeatLimit)
            result.extend(ch1 * addCount)
            freq1 -= addCount
            
            if freq1 > 0:
                if not maxHeap:  
                    break
                
                ord2, freq2 = heapq.heappop(maxHeap)
                ch2 = chr(-ord2)
                
                result.append(ch2)
                freq2 -= 1
                
                if freq2 > 0:
                    heapq.heappush(maxHeap, (ord2, freq2))
                heapq.heappush(maxHeap, (ord1, freq1))
        
        return "".join(result)
        
        