


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	if len(s)==0 or s is None: return 0
    	res,head,tail=0,0,0
    	while tail<len(s)-1:
    		tail +=1
    		if s[tail] not in s[head:tail]:
    			res = max(tail-head+1,res)
			else:
				while s[tail] in s[head:tail]:
					head+=1
		return res
    		

