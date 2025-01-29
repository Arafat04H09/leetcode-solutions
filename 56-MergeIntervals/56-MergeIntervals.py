class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        line = defaultdict(int)

        for start, end in intervals:
            line[start] += 1
            line[end] -= 1
        
        cur = 0
        ans = []
        start = None

        for point in sorted(line.keys()):
            if start is None and cur == 0:
                start = point
            
            cur += line[point]

            if start is not None and cur == 0:
                ans.append([start, point]) #end
                start = None
        
        return ans