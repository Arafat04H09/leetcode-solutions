class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        pre = 0
        cur = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                pre = cur
                cur = 1
            
            if cur <= pre:
                count += 1
        
        return count