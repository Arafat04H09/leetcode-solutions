class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        m = defaultdict(int)

        for x,y in intervals:
            m[x] += 1
            m[y] -= 1
        
        cur = 0
        intervalStart = -1
        ans = []

        for num in sorted(m.keys()):
            if cur == 0: 
                intervalStart = num

            cur += m[num]

            if cur == 0:  
                ans.append([intervalStart, num])
        
        return ans