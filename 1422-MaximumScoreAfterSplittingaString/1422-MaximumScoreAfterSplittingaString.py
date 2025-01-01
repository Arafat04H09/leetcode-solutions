class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = s.count('1')
        zeros = 0
        ans = 0

        for i in range(0, len(s) - 1):
            if s[i] == '0':
                zeros += 1
            if s[i] == '1':
                ones -= 1
            
            ans = max(ans, zeros + ones)
        
        return ans