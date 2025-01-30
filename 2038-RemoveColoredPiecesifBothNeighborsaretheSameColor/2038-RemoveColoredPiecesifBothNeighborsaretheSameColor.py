class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        a = 0
        b = 0

        for i in range(1, len(colors) - 1):
            if colors[i] == 'A' and colors[i - 1] == 'A' and colors[i + 1] ==  'A':
                a += 1
            elif colors[i] == 'B' and colors[i - 1] == 'B' and colors[i + 1] == 'B':
                b+= 1
        
        return a > b         