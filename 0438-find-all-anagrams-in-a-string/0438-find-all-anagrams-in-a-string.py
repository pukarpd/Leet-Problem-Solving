class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): 
            return [] 

        left, right = 0, len(p) - 1 
        res = [] 
        
        newP = Counter(p)
        while right < len(s): 
            mySet = Counter(s[left:right+1])
            # print(mySet, newP)
            if mySet == newP: 
                res.append(left)
            left += 1 
            right += 1
        
        return res

    def quicksort(self, s): 
        s = list(s)
        if len(s) <= 1: 
            return s 
        p = s[-1]
        left = [x for x in s[:-1] if x <= p]
        right = [x for x in s[:-1] if x > p]
        return self.quicksort(left) + [p] + self.quicksort(right)



