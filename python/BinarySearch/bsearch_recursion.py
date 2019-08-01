

from typing import List

def bsearch(nums:List[int],target:int):
	return bsearch_recursion(nums,0,len(nums)-1,target)


def bsearch_recursion(nums:List[int],low:int,high:int,target:int):
	if low > high:
		return -1

	mid = low + (high-low)//2
	if nums[mid] == target:
		return mid
	elif nums[mid] < target:
		return bsearch_recursion(nums,mid+1,high,target)
	else:
		return bsearch_recursion(nums,low,mid-1,target)

if __name__ == '__main__':
	nums = [1,2,4,6,8,9,10]
	target = 10
	res = bsearch(nums,target)
	print(res) # the res is 6


