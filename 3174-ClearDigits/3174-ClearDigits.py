class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        indicesToDelete = set()
        letterIndices = []

        for i, ch in enumerate(s):
            if ch.isdigit(): #delete this and the closest non-digit to its left
                indicesToDelete.add(i)
                if len(letterIndices) > 0:
                    indicesToDelete.add(letterIndices.pop())
            else: #add this letter indice to letterindices
                letterIndices.append(i)
        
        ans = ''

        for i, ch in enumerate(s):
            if i not in indicesToDelete:
                ans += ch
        
        return ans
