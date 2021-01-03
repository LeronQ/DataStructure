
# 26. Remove Duplicates from Sorted Array
# 从有序数据中删除重复元素，并且是原地排序，O(1)的时间复杂度

'''
给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
'''

# 思路：利用双指针，第一个指针temp指向当前不重复的数字的位置，第二个指针从头至尾扫描，当第二个指针与第一个指针的值不同时，
# 说明出现了一个不同的数字，把第一个向后移动一位，并把该数字存入。

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        if len(nums)==1:return 1
        temp = 0
        for i in range(1,len(nums)):
            if nums[temp]!=nums[i]:
                temp +=1
                nums[temp]=nums[i]
        return temp+1