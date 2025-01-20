class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m = {}
        rows = len(mat)
        cols = len(mat[0])

        for row in range(rows):
            for col in range(cols):
                m[mat[row][col]] = (row, col)
        
        sRows = [0] * rows
        sCols = [0] * cols

        for i, num in enumerate(arr):
            row, col = m[num]
            sRows[row] += 1
            sCols[col] += 1

            if sRows[row] == cols or sCols[col] == rows:
                return i
        
        return -1