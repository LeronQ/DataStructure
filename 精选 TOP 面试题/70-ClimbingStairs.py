
# leetcode 70:Climbing Stairs
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
70:Climbing Stairs
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

'''
# 解题思路：经典的动态规划题，类似于青蛙跳阶，走到当前一层阶梯，只能由前一个或者前两个阶梯选择

class Solution:
    def climbStairs(self, n: int) -> int:
        cur = [0]*(n+1)
        cur[0] = 1
        cur[1] = 1
        for i in range(2,n+1):
            cur[i] = cur[i-1]+cur[i-2]

        return cur[n]