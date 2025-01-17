class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        ans = set()

        for start in range(len(s) - 9):
            sequence = s[start: start + 10]
            if sequence in seen:
                ans.add(sequence)
            seen.add(sequence)
        
        return list(ans)