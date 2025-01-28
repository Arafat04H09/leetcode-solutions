class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))  
            total = grid[r][c] 
            
            for dx, dy in dirs:
                total += dfs(r + dx, c + dy)
            
            return total

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and (r, c) not in visited:  
                    ans = max(ans, dfs(r, c))
        
        return ans
