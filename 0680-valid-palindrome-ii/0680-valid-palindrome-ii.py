class Solution:
    def validPalindrome(self, s: str) -> bool:
        # brute force would be to check each one with letter removed. Use two pointers, slide it and if one mismatch is found

        l, r = 0, len(s) - 1 
        while l <= r: 
            if s[l] != s[r]: 
                return self.isPali(s[l+1:r+1]) or self.isPali(s[l:r])
            else: 
                l += 1 
                r -= 1 
        return True

    def isPali(self, s): 
        if s == s[::-1]: 
            return True 
        return False 