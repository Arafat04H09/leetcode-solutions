class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        c1 = Counter(word1)
        c2 = Counter(word2)

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if abs(c1[ch] - c2[ch]) > 3:
                return False
        
        return True