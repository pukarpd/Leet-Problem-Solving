class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    
        hashmap = {} 

        for i in range(len(nums)):
            hashmap[nums[i]] = 0 

        for i in nums: 
            hashmap[i] += 1
        for key, val in hashmap.items(): 
            if val > 1:
                return True 
        return False 