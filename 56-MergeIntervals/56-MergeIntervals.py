class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort() #sort by start

        ans = []
        i = 0
        start = None

        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            while i < len(intervals) and intervals[i][0] <= end: #while next start is in range of prev end
                end = max(end, intervals[i][1])
                i+= 1
            ans.append([start, end])
        
        return ans
        