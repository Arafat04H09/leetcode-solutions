class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        ans = []

        partLen = len(part)
        last = part[-1]  

        for ch in s:
            ans.append(ch)

            if ch == last and len(ans) >= partLen and ''.join(ans[-partLen:]) == part:
                del ans[-partLen:] 
        
        return ''.join(ans)
