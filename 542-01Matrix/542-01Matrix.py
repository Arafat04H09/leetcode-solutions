class Solution(object):
    def updateMatrix(self, mat):
        rows = len(mat) 
        cols = len(mat[0]) 
        dirs = [(0,1), (1, 0), (-1, 0), (0, -1)]
        height = [[-1] * cols for _ in range(rows)]

        queue = deque([])
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    height[row][col] = 0
        
        while queue:
            x, y = queue.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    queue.append((nx, ny))
        
        return height