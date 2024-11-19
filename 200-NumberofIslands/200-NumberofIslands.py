class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return
        
        count = 0 

        def dfs(row, col):
            if row >= len(grid) or row < 0 or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
                return
            else:
                grid[row][col] = '0'
                dfs(row +1, col)
                dfs(row, col + 1)
                dfs (row -1, col)
                dfs(row, col -1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row, col)
                    

        return count