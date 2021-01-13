
# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0: return ""
        # if len(strs)==1: return strs[0]
        min_len = len(strs[0])

        for i in range(len(strs)):
            if len(strs[i])<min_len:
                min_len = len(strs[i])
        res = ""
        
        for i in range(min_len):
            curStr = strs[0][i]
            for j in range(0,len(strs)):
                if strs[j][i] != curStr:
                    return res
            res += curStr
        return res
