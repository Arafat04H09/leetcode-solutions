class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(x, y, group):
            visited[x][y] = True
            group.append((x, y))

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy

                while 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 1 and not visited[nx][ny]:
                        dfs(nx, ny, group)
                    nx += dx
                    ny += dy

        count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and not visited[row][col]:
                    group = []
                    dfs(row, col, group)
                    if len(group) > 1:
                        count += len(group)

        return count