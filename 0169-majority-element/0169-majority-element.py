class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        c = 0 
        cur = None

        for num in nums:
            if c == 0:  
                cur = num 
                c += 1 
            elif cur == num:
                c += 1 
            else: 
                c -= 1 

        return cur 
