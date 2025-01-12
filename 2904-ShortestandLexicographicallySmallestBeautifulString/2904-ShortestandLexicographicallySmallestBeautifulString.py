class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        smallest = float("inf")
        numOnes = 0
        start = 0

        for end in range(len(s)):
            if s[end] == '1':
                numOnes += 1
            
            while start < end and numOnes > k:
                if s[start] == "1":
                    numOnes -= 1
                start += 1

            if numOnes == k:
                curNum = int(''.join(s[start:end + 1]))
                smallest = min(smallest, curNum)

        return str(smallest) if smallest != float("inf") else ""

