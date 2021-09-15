组合 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 你可以按 任何顺序 返回答案。 示例 1：
输入：n = 4, k = 2 输出： [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ] 示例 2：
输入：n = 1, k = 1 输出：[[1]]
提示：
1 <= n <= 20 1 <= k <= n

class Solution:
    def combine(self, n: int, k: int):
        res=[]  #存放符合条件结果的集合
        path=[]  #用来存放符合条件结果
        def backtrack(n, k, startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex, n-(k-len(path))+2):  #优化的地方
                path.append(i)  #处理节点
                backtrack(n, k, i+1)  #递归
                path.pop()  #回溯，撤销处理的节点
        backtrack(n, k, 1)
        print(res)
        return res

# vector<int> temp;
# void dfs(int cur, int n) {
#     if (cur == n + 1) {
#         // 记录答案
#         // ...
#         return;
#     }
#     // 考虑选择当前位置
#     temp.push_back(cur);
#     dfs(cur + 1, n, k);
#     temp.pop_back();
#     // 考虑不选择当前位置
#     dfs(cur + 1, n, k);
# }

class Solution:
    def combine(self, n: int, k: int):
        res=[]  #存放符合条件结果的集合
        path=[]  #用来存放符合条件结果
        def backtrack(n, k, startIndex):
            if startIndex == n+1:
                res.append(path[:])
                return
            path.append(startIndex)
            backtrack(n, k, startIndex+1)
            path.pop()
            backtrack(n, k, startIndex+1)
        backtrack(n, k, 1)
        print(res)
        return res

s = Solution()
s.combine(4, 2)
1
