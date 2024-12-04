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
        n2 = len(str2)

        for ch in str1:
            next_ch = 'a' if ch == 'z' else chr(ord(ch) + 1)
            
            if ch == str2[i2] or next_ch == str2[i2]:
                i2 += 1
                if i2 == n2:
                    return True

        
        return False


