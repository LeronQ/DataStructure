

# leetcode 53:最大子序和
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大为 6。

'''

'''
	解题思路： 动态规划
	如果当前num[i]小于0，则最大子序和一定不包括当前值，同时为了节省内存空间,重新将num[i]表示为累计到第i个序列的最大值
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] +=  max(nums[i-1],0)
        return max(nums)