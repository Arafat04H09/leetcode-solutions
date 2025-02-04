class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        dirs = [(1,0), (0, 1), (-1, 0), (0, -1)]
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and board[r][c] == 'O':
                visited.add((r,c))
                
                for dx, dy in dirs:
                    dfs(r + dx, c + dy)

        for r in range(0, rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        for c in range(0, cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X' 
         


