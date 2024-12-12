class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        deviceCounts = [row.count('1') for row in bank if row.count('1') > 0]
        
        totalBeams = 0
        for i in range(1, len(deviceCounts)):
            totalBeams += deviceCounts[i] * deviceCounts[i - 1]
        
        return totalBeams
