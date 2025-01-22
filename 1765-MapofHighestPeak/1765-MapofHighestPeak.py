class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(isWater)
        cols = len(isWater[0])
        dirs = [(0,1), (1, 0), (-1, 0), (0, -1)]
        height = [[-1] * cols for _ in range(rows)]

        queue = deque([])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    height[r][c] = 0
                    queue.append((r, c))
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    queue.append((nx, ny))
        
        return height