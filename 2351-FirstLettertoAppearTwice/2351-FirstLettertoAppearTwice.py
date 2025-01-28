class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen:
                return ch
            
            seen.add(ch)
        
        return -1