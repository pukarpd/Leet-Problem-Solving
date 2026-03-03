class Solution:
    def __init__(self): 
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"

        self.r1 = set(x for x in r1)
        self.r2 = set(x for x in r2)
        self.r3 = set(x for x in r3)
    def findWords(self, words: List[str]) -> List[str]:
        res = []

        # print(f"{self.r1}\n{self.r2}\n{self.r3}")
        for word in words: 
            mySet = set(l.lower() for l in word)
            print(mySet)
            if (mySet | self.r1 == self.r1 or 
                mySet | self.r2 == self.r2 or 
                mySet | self.r3 == self.r3
            ): 
                res.append(word)

        return res


        