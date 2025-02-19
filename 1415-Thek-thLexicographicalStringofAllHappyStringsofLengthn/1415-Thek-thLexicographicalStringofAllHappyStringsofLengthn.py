class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        
        def backtrack(cur):
            if len(cur) == n:
                res.append(cur)
                return
            
            for letter in ['a', 'b', 'c']:
                if not cur or cur[-1] != letter:
                    backtrack(cur + letter)
        
        backtrack("")  # Start with an empty string.
        return res[k - 1] if k <= len(res) else ""