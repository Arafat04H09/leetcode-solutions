class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backtrack(open, close, s):
            if len(s) == n * 2:
                ans.append(s)
                return
            
            if open < n:
                backtrack(open + 1, close, s + '(')

            if close < open: 
                backtrack(open, close + 1, s + ')')

        backtrack(0,0,'')
        return ans        