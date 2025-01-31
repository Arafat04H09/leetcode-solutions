class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #get areas of island

        #checck if changing a 0 to a 1 connects any islands 

        # keep track of max size island u can make
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        sizes = defaultdict(int)
        islandNum = 2
        m = 0

        def dfs(row, col, islandNum):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                grid[row][col] = islandNum
                sizes[islandNum] += 1

                for dx, dy in dirs:
                    nx, ny = row + dx, col + dy

                    dfs(nx, ny, islandNum) #find everything on the island

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c, islandNum)
                    m = max(m, sizes[islandNum])
                    islandNum += 1 #find all diff islands
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: #if water
                    combinedSize = 0
                    connected = set()
                    for dx, dy in dirs:
                        nx, ny = r + dx, c + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] > 1:
                            if grid[nx][ny] not in connected:
                                combinedSize += sizes[grid[nx][ny]]
                                connected.add(grid[nx][ny])
                    m = max(m, combinedSize + 1)
        
        return m
