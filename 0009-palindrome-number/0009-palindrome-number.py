class Solution:
    def isPalindrome(self, x: int) -> bool:

        x = str(x)

        if len(x) == 2: 
            if x[0] != x[1]:
                return False
        a = 0
        b = len(x) - 1
        c = len(x) / 2 

        while a <= c and b >= c:
            if x[a] == x[b]: 
                a += 1 
                b -= 1
            else:
                return False
        
        return True 