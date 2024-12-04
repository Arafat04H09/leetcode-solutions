class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if len(str2) > len(str1):
            return False
        
        if len(str2) == 0:
            return True

        i2 = 0

        def nextChar(ch):
            if ch == 'z':
                return 'a'
            else:
                return chr(ord(ch) + 1)

        for _, ch in enumerate(str1):
            if ch == str2[i2] or nextChar(ch) == str2[i2]:
                i2 += 1
            if i2 == len(str2):
                return True
        
        return False


