class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def isSubstring(s):
            return s == s[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                if isSubstring(s[start: end + 1]):
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return res