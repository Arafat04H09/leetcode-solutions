class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        rSet = [set() for _ in range(rows)]
        cSet = [set() for _ in range(cols)]
        bSet = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(rows):
            for c in range(cols):
                num = board[r][c]
                if num == '.':
                    continue
                if num in rSet[r] or num in cSet[c] or num in bSet[r//3][c//3]:
                    return False
                rSet[r].add(num)
                cSet[c].add(num)
                bSet[r//3][c//3].add(num)
        
        return True