class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {} 

        for i in nums: 
            hashmap[i] = 0 

        for i in range(len(nums)): 
            hashmap[nums[i]] += 1 
        
        for key, value in hashmap.items(): 
            if value > 1: 
                return key 
