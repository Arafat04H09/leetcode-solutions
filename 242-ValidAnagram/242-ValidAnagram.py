class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = defaultdict(int)

        for ch in s:
            m[ch] += 1
        
        for ch in t:
            m[ch] -= 1
        
        return all(value == 0 for value in m.values())