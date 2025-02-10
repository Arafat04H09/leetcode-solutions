class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        for i, ch in enumerate(s):
            if ch.isdigit(): 
                if len(ans) > 0: #remove the laast character in the ans 
                    ans.pop()
            else: 
                ans.append(ch)

        return ''.join(ans)
