class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        l1 = len(start)
        l2 = len(target)
        if l1 != l2:
            return False
        
        if start.count("R") != target.count("R") or start.count("L") != target.count("L"):
            return False

        if start == target: 
            return True
        
        startIndex = 0
        targetIndex = 0

        while startIndex < l1 and targetIndex < l2:
            while startIndex < l1 and start[startIndex] == '_':
                startIndex += 1
            
            while targetIndex < l2 and target[targetIndex] == '_':
                targetIndex += 1 

            if startIndex == l1 or targetIndex == l2:
                break

            if start[startIndex] != target[targetIndex]:
                return False
            elif start[startIndex] == 'R' and targetIndex < startIndex:
                return False
            elif start[startIndex] == 'L' and targetIndex > startIndex:
                return False

            startIndex += 1
            targetIndex += 1 

        return True
