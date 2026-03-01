# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # solved test cases in less than 5 mins, right intuition wrong appraoch.  
        if guess(n) == 0: 
            return n
        lo, hi = 1, n 

        while lo <= hi: 
            mid = (lo + hi) // 2 
            pick = guess(mid)
            # print(n)
            if pick == -1:   
                hi = mid
            elif pick == 1: 
                lo = mid 
            else: 
                return mid