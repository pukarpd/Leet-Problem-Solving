class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.sort()
        
        res = []
        start = 0 

        for i in range(1, len(nums)): 
            if nums[i] != nums[i-1] + 1: 
                res.append(nums[start:i])
                start = i 
        if nums: 
            res.append(nums[start:])
        
        res2 = []
        for item in res: 
            temp = ''
            if len(item) == 1: 
                temp += str(item[0])
            else: 
                temp += str(item[0])+'->'+str(item[-1])
            res2.append(temp)
        return res2
            



             

