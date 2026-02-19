class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Own Solution
        # O(n * k) where k == len(s1) and n == len(s2)

        compare = Counter(s1)

        i, j = 0, (len(s1) - 1)

        while j < len(s2): 
            substring = s2[i:j+1]
            temp = Counter(substring)
            res = 0 
            for k, v in temp.items(): 
                if k in temp and temp[k] == compare[k]: 
                    res += 1 
            if res == len(temp): 
                return True
            i += 1 
            j += 1 

        return False

        # # O(klogk * n )
        # s1 = ''.join(sorted(s1))

        # i, j = 0, len(s1) - 1 

        # while j < len(s2): 
        #     sComp = ''.join(sorted(s2[i:j+1]))

        #     if s1 == sComp: 
        #         return True 
        #     i += 1 
        #     j += 1 
        # return False
