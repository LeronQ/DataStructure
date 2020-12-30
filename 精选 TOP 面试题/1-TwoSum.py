
# leetcode 1:Two Sum

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''


'''
 解题思路： 用一个字典维护，元素如果没有出现在字典key中,则key为target与key的差值，value为其索引；
			如果出现，表明之前num[i]中当前值的和为target了,因此输出其索引即可
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<=1:return None
       
        nums_dict = {}
        for i, num in enumerate(nums):
            if num in nums_dict:
                return [nums_dict[num], i]
            else:
                nums_dict[target - num] = i
        

