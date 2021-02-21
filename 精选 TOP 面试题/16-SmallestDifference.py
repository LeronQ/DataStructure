

class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a,b=sorted(a),sorted(b)
        m,n = len(a),len(b)
        i,j,res=0,0,float("inf")
        while i<m and j<n:
            res = min(res,abs(a[i]-b[j]))
            if a[i]<b[j]:
                i +=1
            else:
                j +=1
        return res
