'''
two pointers, l and r 
res which is maxlen, update when we dont see duplicates
if there is a duplicate in the window, its no longer valid, and we have to shift the l pointer to the right. 

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0 

        if len(s) == 1: 
            return 1

        # eatew
        maxLen = 1
        l, r = 0, 1 

        compare_window = set()
        while r < len(s): 
            compare_window = set([i for i in s[l:r]])

            if s[r] not in compare_window: 
                maxLen = max(len(s[l:r+1]), maxLen)
                r += 1 
            else: 
                l += 1  
                
     
        return maxLen
