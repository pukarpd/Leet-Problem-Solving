class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        for i in range(len(s)):
            arr.append(s[i])
        res = []
        starcount = 0
        while arr: 
            while arr and arr[-1] == '*': 
                print(starcount, arr[-1])
                arr.pop()
                starcount += 1
            while arr and starcount > 0: 
                if arr[-1] == '*': 
                    break
                print(starcount, arr[-1])
                arr.pop()
                starcount -= 1
                
            if arr and arr[-1] != '*' and starcount == 0:
                res.append(arr.pop())
        res.reverse()
        return ''.join(res)
            
             

