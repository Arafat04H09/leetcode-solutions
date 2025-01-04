class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = defaultdict(int)
        last = defaultdict(int)
        unique = set()

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        ways = 0

        for char in first:
            if first[char] < last[char]:
                ways += len(set(s[first[char] + 1 : last[char]]))
        
        return ways
            


