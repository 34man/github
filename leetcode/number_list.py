# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def step(row, col):
            # print(row, col)
            if row == m or col == n:
                return 1
            else:
                return step(row+1, col) + step(row, col+1)
        return step(1, 1)
s = Solution()
s.uniquePaths(23, 12)
