class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''

        longest = s[0]
        l = len(s)
        dp = [[False] * l for _ in range(l)]

        for i in range(l):
            dp[i][i] = True
        
        for start in range(l - 1, -1, -1):
            for end in range(start + 1, l):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                    
                        if end - start + 1 > len(longest):
                            longest = s[start: end + 1]
        
        return longest
