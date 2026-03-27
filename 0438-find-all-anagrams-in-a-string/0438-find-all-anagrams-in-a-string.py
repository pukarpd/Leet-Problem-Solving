class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): 
            return []

        p = sorted(p)
        print(p)
        left, right = 0, len(p) - 1 
        res = []

        while right < len(s): 
            curString = s[left:right+1]
            sortedString = sorted(curString)
            # print(f"sortedstring:{sortedString}")
            if sortedString == p: 
                res.append(left)
            left += 1 
            right += 1 

        return res
            

    # def quicksort(self, s): 
    #     s = list(s)
    #     if len(s) <= 1: 
    #         return s 
        
    #     pivot = s[-1]
    #     index = 0
    #     for i in range(len(s)):
    #         if ord(pivot) < s[i]: 
    #             s[i], pivot = pivot, s[i]
    #             index = i
        
    #     return self.quicksort(s[:index+1]) + self.quicksort(s[index:])



