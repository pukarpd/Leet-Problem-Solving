class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, reslen = "", 0 
        # Single pass, expand from middle two pointers palindromic dp invariant, never seen this pattern, cool solution
        # this is done for each part of the string. 
        for i in range(len(s)):
            # odd length palindromes 
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r-l+1) > reslen: 
                    res = s[l:r+1]
                    reslen = (r-l + 1)
                l -= 1 #loop breaks here 
                r += 1 
            # check for even length palindromes
            l, r = i, i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r-l+1) > reslen: 
                    res = s[l:r+1]
                    reslen = (r-l+1)
                l-=1
                r+=1
        
        return res
        






        











    #     # brute force should be acceptable since s.length <= 1000 O(n^3)
    #     maxLength = [0, ''] 
    #     for i in range(len(s)): 
    #         for j in range(len(s)):
    #             if s[i:j+1] == self.reverse(s[i:j+1]):
    #                 maxLength[0] = max(maxLength[0], len(s[i:j+1]))
    #                 if len(s[i:j+1]) == maxLength[0]: 
    #                     maxLength[1] = s[i:j+1]


    #     return maxLength[1] 

    def reverse(self, s): 
        res = ''

        for i in range(len(s)-1,-1,-1): 
            res += s[i]

        return res 
