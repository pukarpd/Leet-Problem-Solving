class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        sm = self.mappings(s)
        tm = self.mappings(t)
        
        return sm == tm
    def mappings(self, s):
        myMap = defaultdict(list)
        for i in range(len(s)): 
            myMap[s[i]].append(i)

        return sorted([val for val in myMap.values()])




        # Failed Soln
    #     if len(s) == 1: 
    #         return True 

    #     if len(s) == 2 and len(set(s)) == len(set(t)): 
    #         return True
    #     elif len(s) == 2:
    #         return False
        
    #     sl = self.find(s)
    #     tl = self.find(t)
    #     print(sl, tl)

    #     return sl == tl


    # def find(self, s): 
    #     res = []
    #     l, r = 0, 1

    #     while r < len(s): 
    #         if s[l] != s[r]: 
    #             res.append(len(s[l:r]))
    #             l = r
    #         r += 1 
    #     print(r,l)
    #     if l == r -1: 
    #         r -= 1 
    #         l -= 1  
    #     else: 
    #         r -= 1 

    #     if s[l] != s[r]: 
    #         res.append(1)
    #     elif s[l] == s[r]: 
    #         res.append(2)
        
    #     return res    

