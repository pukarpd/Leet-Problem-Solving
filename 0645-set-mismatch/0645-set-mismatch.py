class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numCount = Counter(nums)
        numSet = set(nums)
        setcmp = set()
        for i in range(1, n+1): 
            setcmp.add(i)

        res = [] 
        missingVal = (setcmp - numSet)
        
         
        for k, v in numCount.items(): 
            if v > 1: 
                res.append(k)

        for v in missingVal: 
            res.append(v)

        return res