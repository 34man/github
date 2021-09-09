在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。

给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

注意：分割得到的每个字符串都必须是平衡字符串。

返回可以通过分割得到的平衡字符串的 最大数量 。

 

示例 1：

输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL"、"RRLL"、"RL"、"RL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ant = 0
        R = 0
        L = 0
        for i in s:
            if i == 'L':
                L += 1
            else:
                R += 1
            if R == L:
                R, L = 0, 0
                ant += 1
        return ant
s = Solution()
s.balancedStringSplit('RLRLRRLL')

11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，
垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

class Solution:
    def maxArea(self, height):
        right = len(height)
        max_con = 0
        for i in range(1, right):
            for j in range(i):
                content = (i-j)*min(height[i], height[j])
                if content>max_con:
                    max_con = content
        return max_con
s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])


class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        max_con = 0
        while left < right:
            content = (right-left)*min(height[left], height[right])
            if content>max_con:
                max_con = content
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_con

134. 加油站
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明:

如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。
示例 1:

输入:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]


输出: 3

解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        start = 0
        long = len(gas)
        while start < long:
            bag = gas[start]
            for i in range(start, start+long):
                step = i%long
                bag = bag - cost[step]
                if bag < 0:
                    break
                bag += gas[(i+1)%long]
            if bag >= 0:
                return start
            start += 1
        return -1

s = Solution()
s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])



135. 分发糖果
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？



示例 1：

输入：[1,0,2]
输出：5
解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。

class Solution:
    def candy(self, ratings) -> int:
        candys = [1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i] > ratings[i+1]:
                candys[i] += 1
        if ratings[-1]>ratings[-2]:
            candys[-1] = candys[-2] + 1
        print(candys)
        return sum(candys)

s = Solution()
s.candy([1, 0, 2])

pass
