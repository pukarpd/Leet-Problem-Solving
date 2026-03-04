class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        # this is done for each part of the string. 
        for i in range(len(s)):
            # odd length palindromes 
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                res+= 1 
                l -= 1 #loop breaks here 
                r += 1 
            # check for even length palindromes
            l, r = i, i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                res += 1 
                l-=1
                r+=1
        
        return res
