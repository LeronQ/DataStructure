

from typing import List

def bsearch(nums:List[int],target:int):
	'''
		该方法是在给定一个有序并且五重复值的数组中，通过二分查找方法，找到给定目标值在
		数组中的索引，如果该值不存在，则返回-1
	'''
	low = 0
	high = len(nums) -1 
	while low < high:
		mid = low + (high - low ) //2
		if nums[mid] == target:
			return mid
		elif nums[mid] < target :
			low = mid + 1
		else:
			high = mid -1
	
	return -1

if __name__ == '__main__':
	nums = [1,2,4,6,8,9,10]
	target = 10
	res = bsearch(nums,target)
	print(res) # the res is 6