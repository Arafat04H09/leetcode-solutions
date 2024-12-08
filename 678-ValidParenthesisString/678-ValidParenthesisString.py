class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min_open = 0
        max_open = 0

        for ch in s:
            if ch == '(':
                min_open += 1
                max_open += 1
            elif ch == ')':
                min_open = max(0, min_open - 1)
                max_open -= 1
            else:  
                min_open = max(0, min_open - 1)
                max_open += 1
            
            if max_open < 0:
                return False

        return min_open == 0
