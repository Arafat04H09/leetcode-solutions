class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        rows, cols = len(heightMap), len(heightMap[0])
        if rows < 3 or cols < 3:
            return 0
        
        heap = []
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    heapq.heappush(heap, (heightMap[row][col], row, col))
                    heightMap[row][col] = -1
        
        level, ans = 0, 0

        while heap:
            height, row, col = heapq.heappop(heap)
            level = max(level, height)
            dirs = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

            for newRow, newCol in dirs:
                if 0 <= newRow < rows and 0 <= newCol < cols and heightMap[newRow][newCol] != -1:
                    heapq.heappush(heap, (heightMap[newRow][newCol], newRow, newCol))
                    ans += max(0, level - heightMap[newRow][newCol])

                    heightMap[newRow][newCol] = -1
        
        return ans
