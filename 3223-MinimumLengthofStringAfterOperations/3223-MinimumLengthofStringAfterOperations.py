class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        indices = defaultdict(int)
        deleted = 0

        for i, ch in enumerate(s):
            indices[ch] += 1
        
        for numIndices in indices.values():
            if numIndices > 2:
                deleted += numIndices - 1 if numIndices % 2 == 1 else numIndices - 2
        
        return len(s) - deleted