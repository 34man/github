# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？

# 超出时间限制的解法
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def step(row, col):
            # print(row, col)
            if row == m or col == n:
                return 1
            else:
                return step(row+1, col) + step(row, col+1)
        return step(1, 1)


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划计算总共有多少个种类
        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2

class Solution:
    # 动态规划，这里用一维dp记录每一行的结果，上一行的结果复刻到下一行进行操作
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 - obstacleGrid[0][0]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue
                if j > 0 and obstacleGrid[i][j-1] == 0:
                    dp[j] += dp[j-1]
                print(i, j, dp)
        return dp[n-1]

class Solution:
    # 动态规划，这里用一维dp记录每一行的结果，上一行的结果复刻到下一行进行操作
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0]*n
        dp[0] = 1-obstacleGrid[0][0]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                if j > 0 and obstacleGrid[i][j-1] == 0:
                    dp[j] += dp[j-1]
        return dp[-1]
s = Solution()
s.uniquePathsWithObstacles([[0,0,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]])
