class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        m = defaultdict(int)
        lastPosionTime = -1
        c = 0
        totalTime = 0

        for time in timeSeries:
            m[time] += 1
            m[time + duration] -= 1
        
        for num in sorted(m):
            if c == 0:
                lastPoisonTime = num
            
            c += m[num]

            if c == 0:
                totalTime += (num - lastPoisonTime)
        
        return totalTime