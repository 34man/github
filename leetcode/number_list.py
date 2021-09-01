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


# 34. 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。
# nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]

# class Solution:
#     def searchRange(self, nums, target):
#         mild = len(nums)//2
#         if len(nums) < 2:
#             return [-1, -1]
#         elif nums[mild] > target:
#             return self.searchRange(nums[:mild], target)
#         elif nums[mild] < target:
#             return self.searchRange(nums[mild:], target)
#         elif nums[mild] == target:
#             if nums[mild-1] == target:
#                 return [mild-1, mild]
#             else:
#                 return [mild, mild+1]
#         else:
#             return [-1, -1]
#
# s = Solution()
# s.searchRange([1,1,2,2,3,4,5], 5)

# 二分法寻找
class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mild = (right - left)//2 + 1
            if nums[mild] < target:
                left = mild
            elif nums[mild] > target:
                right = mild
            elif nums[mild] == target:
                left = self.searchRange(nums[: mild+1], target)
                right = self.searchRange(nums[mild-1:], target)

        return [left, right]
s = Solution()
s.searchRange([1,2,3], 2)

# 二分法基础
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while 1:
            mild = (right-left) // 2
            if nums[mild] == target:
                return mild
            elif nums[mild] > target:
                right = mild - 1
            elif nums[mild] < target:
                left = mild + 1
            else:
                return -1

s = Solution()
s.search([1,2,3,4], 4)



给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
class Solution:
    def minPathSum(self, grid):
        dp = [100000]*len(grid[0])
        dp[0] = grid[0][0]
        for tip, ele in enumerate(grid):
            for i, num in enumerate(ele):
                if i > 0:
                    dp[i] = min(dp[i-1] + num, dp[i] + num)
                    print(dp)
                if i == 0 and tip != 0:
                    dp[i] = dp[0] + num
        print(dp)
        return dp[-1]
s = Solution()
s.minPathSum([[1,2,3], [4,5,6]])

一维数组动态规划
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [100000]*len(grid[0])
        dp[0] = grid[0][0]
        for tip, ele in enumerate(grid):
            for i, num in enumerate(ele):
                if i > 0:
                    dp[i] = min(dp[i-1] + num, dp[i] + num)
                if i == 0 and tip != 0:
                    dp[i] = dp[0] + num
        return dp[-1]

一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。
我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；
其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。

为了尽快到达公主，骑士决定每次只向右或向下移动一步。

class Solution:
    def calculateMinimumHP(self, dungeon):
        dp = [[sum(dungeon[0])+1, 0] for _ in range(len(dungeon[0]))]
        dp[0][0] = dungeon[0][0]
        dp[0][1] = dungeon[0][0]

        for i, eles in enumerate(dungeon):
            for j, ele in enumerate(eles):
                print(dp)
                if i == 0:
                    if j > 0:
                        dp[j][0] = min(dp[j-1][0]+ele, dp[j-1][0])
                        dp[j][1] = dp[j-1][1]+ele
                else:
                    if j > 0:
                        tip1 = 0 if ele+dp[j-1][0]+dp[j-1][1]>0 else ele+dp[j-1][0]+dp[j-1][1]
                        tip2 = 0 if ele+dp[j][0]+dp[j-1][1]>0 else ele+dp[j][0]+dp[j-1][1]
                        dp[j][0] = min(max(tip1, tip2), dp[i-1][0])
                        dp[j][1] = max(ele+dp[j-1][1], dp[j][1]+ele)
                    else:
                        dp[j][0] = min(dp[j][0]+ele, dp[j][0])
                        dp[j][1] = dp[j][1]+ele
        print(dp)
        return 0 if dp[0][0]>0 else -dp[0][0]
s = Solution()
s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])


-2 -3  3
-5 -10 1
10 30 -5


[[1, 0]]*2


pass
