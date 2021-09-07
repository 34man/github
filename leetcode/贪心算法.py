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




pass
