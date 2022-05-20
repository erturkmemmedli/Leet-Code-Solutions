class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:        
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, len(obstacleGrid)):
            obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
        for j in range(1, len(obstacleGrid[0])):
            obstacleGrid[0][j] = obstacleGrid[0][j-1] * (1 - obstacleGrid[0][j])
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1 - obstacleGrid[i][j])
        return obstacleGrid[-1][-1]
