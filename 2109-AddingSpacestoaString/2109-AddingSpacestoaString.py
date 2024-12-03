class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        spaceIndex = 0
        res = []
        n = len(spaces)

        for i, ch in enumerate(s):
            if spaceIndex < n and i == spaces[spaceIndex]:
                res.append(' ')
                spaceIndex += 1
            res.append(ch)
        
        return ''.join(res)
