
# leetcode 7: Reverse Integer

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
'''
# method 1: 直接反转,利用数组的[::-1]进行倒序排列
class Solution:
    def reverse(self, x: int) -> int:
        if x==0: return 0
        if x<((-2)**31-1) or x>((2**31)-1):
            return 0 
        strnum = str(abs(x))
        strnum = int(strnum[::-1])
        if strnum<((-2)**31-1) or strnum>((2**31)-1):
            return 0
        if x<0:
            return -strnum
        return strnum


# method 2： 字符串拼接反转,字符串反向拼接
class Solution:
    def reverse(self, x: int) -> int:
        if x==0: return 0
        if x<((-2)**31-1) or x>((2**31)-1):
            return 0 
         res =''
         strnum = str(abs(x))
         for i in range(len(strnum)):
             res = strnum[i]+res
         if x<0:
             res = -int(res)
         else:
             res = int(res)
         if res<((-2)**31-1) or res>((2**31)-1):
            return 0
        return res
       