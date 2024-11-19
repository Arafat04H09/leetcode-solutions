class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        m = defaultdict(int)
        c = 0
        start = -1

        if newInterval in intervals:
            return intervals

        for x,y in intervals:
            m[x] += 1
            m[y] -= 1
        m[newInterval[0]] += 1
        m[newInterval[1]] -= 1

        for num in sorted(m):
            if c == 0:
                start = num
            
            c += m[num] 

            if c == 0:
                ans.append([start, num])
        
        return ans