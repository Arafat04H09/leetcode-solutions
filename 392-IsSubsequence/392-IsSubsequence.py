class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        
        if len(t) < len(s):
            return False
        
        i = 0

        for ch in t:
            if ch == s[i]:
                i += 1
            if i == len(s):
                return True
    
        return False

        