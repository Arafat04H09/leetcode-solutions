class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        diffPair = []

        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diffPair.append((c1, c2))
                if len(diffPair) > 2:
                    return False
        
        return len(diffPair) == 2 and diffPair[0] == diffPair[1][::-1] 