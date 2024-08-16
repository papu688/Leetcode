class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        
        if not s1[0] == s2[0] == s3[0]:
            return(-1)

        a,b,c = len(s1), len(s2), len(s3)
        minLen = min(a,b,c)

        res = a + b + c 

        for i in range(minLen):
            if s1[i]==s2[i]==s3[i]:
                res -= 3
            else:
                break
            
        return res
