class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        m = defaultdict(int)
        count = 0

        for duration in time:
            count += m[(60 - duration % 60) % 60]  
            m[duration % 60] += 1  
        
        return count
