class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        n = len(s)
        prev2, prev = 1, 1

        for i in range(1, n + 1):
            cur = 0
            if s[i - 1] != '0':
                cur += prev
            
            if i > 1 and 10 <= int(s[i - 2: i]) <= 26:
                cur += prev2
            
            prev, prev2 = cur, prev
            
        return prev