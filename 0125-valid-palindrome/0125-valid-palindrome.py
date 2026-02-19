class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        comp = ''
        for i in range(len(s)): 
            if s[i].isalnum():
                comp += s[i].lower()
        
        l, r = 0, len(comp) - 1 

        while l <= r: 
            # print(l,r)
            if comp[l] != comp[r]: 
                return False 
            l += 1 
            r -= 1 
        return True