class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[1])
        idx = 0 
        prevEnd = -100000
        count = 0

        while idx < len(intervals):
            if intervals[idx][0] < prevEnd: #if current start greater than previous end 
                count += 1
                idx += 1
                continue
            prevEnd = intervals[idx][1]
            idx += 1
        
        return count