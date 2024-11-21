class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [['U'] * n for _ in range(m)]
        
        for r, c in guards:
            grid[r][c] = 'G'
        for r, c in walls:
            grid[r][c] = 'W'
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for r, c in guards:
            for dr, dc in directions:
                curR, curC = r, c
                while 0 <= curR + dr < m and 0 <= curC + dc < n:
                    curR += dr
                    curC += dc
                    if grid[curR][curC] in ('G', 'W'): 
                        break
                    if grid[curR][curC] == 'U':  
                        grid[curR][curC] = 'V'

        unguarded = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'U':
                    unguarded += 1
        
        return unguarded
