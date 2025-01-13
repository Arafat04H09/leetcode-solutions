class Solution(object):
    def __init__(self):
        self.dic = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (s1, s2) in self.dic:
            return self.dic[(s1, s2)]
        
        if s1 == s2:
            self.dic[(s1, s2)] = True
            return True

        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.dic[(s1, s2)] = True
                return True

            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                self.dic[(s1, s2)] = True
                return True
        
        self.dic[(s1, s2)] = False
        return False

        
        
       