class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()

        ans = ''

        for word in s[::-1]:
            ans += word + ' '
        
        return ans.strip()