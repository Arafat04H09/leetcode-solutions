class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        m = {}

        for sCharacter, tCharacter in zip(s, t):
            if sCharacter in m:
                if m[sCharacter] != tCharacter:
                    return False
            else:
                if tCharacter in m.values():
                    return False
                m[sCharacter] = tCharacter

        return True