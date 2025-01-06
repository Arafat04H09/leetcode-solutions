class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        fromLeft = [0] * n
        fromRight = [0] * n

        onesCounted = 1 if boxes[0] == '1' else 0
        for i in range(1, n):
            fromLeft[i] = fromLeft[i - 1] + onesCounted

            if boxes[i] == '1':
                onesCounted += 1
        
        onesCounted = 1 if boxes[-1] == '1' else 0
        for i in range(n - 2, -1, -1):
            fromRight[i] = fromRight[i + 1] + onesCounted
            
            if boxes[i] == '1':
                onesCounted += 1
        
        return [fromLeft[i] + fromRight[i] for i in range(n)]
        
