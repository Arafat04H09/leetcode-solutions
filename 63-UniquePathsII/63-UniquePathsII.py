class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        res = [[0] * cols for _ in range(rows)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            return 0
        else:
            res[0][0] = 1

        for i in range(rows):  
            for j in range(cols): 
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0  
                else:
                    if i-1 >= 0:
                        res[i][j] += res[i-1][j]
                    if j-1 >= 0:
                        res[i][j] += res[i][j-1]
        return res[rows - 1][cols - 1]
