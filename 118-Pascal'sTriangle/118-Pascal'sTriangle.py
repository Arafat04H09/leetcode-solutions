class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]

        triangle = [[1], [1,1]]

        for row in range(3, numRows + 1):
            curRow = [1]
            prevRow = triangle[-1]
            i = 1
            while i < len(prevRow):
                curRow.append(prevRow[i - 1] + prevRow[i])
                i += 1

            curRow.append(1)
            triangle.append(curRow)

        return triangle 