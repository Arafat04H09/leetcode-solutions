class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def dfs(s, o, c):
            if len(s) == n * 2:
                ans.append(s)
                return

            if o < n:
                dfs(s + '(', o + 1, c)
            
            if c < o:
                dfs(s + ')', o, c + 1)
            
        dfs('',0,0)

        return ans