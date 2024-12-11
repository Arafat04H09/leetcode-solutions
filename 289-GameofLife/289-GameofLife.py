class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        r = len(board)
        c = len(board[0])
        scores = [[0] * c for _ in range(r)]

        for row in range(r):
            for col in range(c):
                if board[row][col] == 1:
                    for x, y in dirs:
                        if row + x < r and row + x > -1 and col + y < c and col + y > -1:
                            scores[row + x][col + y] += 1
        
        for row in range(r):
            for col in range(c):
                if board[row][col] == 0:
                    if scores[row][col] == 3:
                        board[row][col] = 1
                else:
                    if scores[row][col] < 2 or scores[row][col] > 3:
                        board[row][col] = 0
        