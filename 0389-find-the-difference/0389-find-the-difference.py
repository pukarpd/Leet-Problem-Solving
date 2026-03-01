class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
     
        mapS = Counter(s)
        mapT = Counter(t)

        for k, v in mapT.items():
            if k not in mapS or mapS[k] < mapT[k]: 
                return k

     
