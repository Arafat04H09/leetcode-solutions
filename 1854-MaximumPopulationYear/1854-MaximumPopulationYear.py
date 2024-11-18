class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        changes = defaultdict(int)

        for birth, death in logs:
            changes[birth] += 1
            changes[death] -= 1

        m = 0
        c = 0
        myear = 0

        for year in sorted(changes):
            c += changes[year]

            if c > m:
                myear = year
                m = c 
        
        return myear