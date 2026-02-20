class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0 
        j = len(s) - 2 

        for i in range(len(s)-1,0,-1): 
            res += abs(ord(s[i]) - ord(s[j]))
            j -= 1 
        return res