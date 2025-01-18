class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque([(0, 0, 0)])

        while q:
            cost, x, y = q.popleft()

            if visited[x][y]:
                continue
            visited[x][y] = True   
        
            if x == rows - 1 and y == cols - 1:
                return cost

            for i, (dx, dy) in enumerate(dirs):
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[x][y] == i + 1:
                        q.appendleft((cost, nx, ny))  
                    else:
                        q.append((cost + 1, nx, ny))

        return -1
            




