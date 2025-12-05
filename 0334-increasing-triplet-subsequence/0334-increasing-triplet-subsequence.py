class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) == 1 or len(nums) == 2: 
            return False 

        if len(nums) == 3: 
            return True if nums[0] < nums[1] and nums[1] < nums[2] else False
        
        i, j, k = 0, 1, 2

        while i < len(nums) - 2: 
            if nums[i] < nums[j] and nums[j] < nums[k]: 
                return True
            elif nums[i] > nums[j]: 
                i += 1 
                j = i + 1 
                k = j + 1 
            elif nums[i] < nums[j] and nums[j] > nums[k]: 
                while nums[j] > nums[k]: 
                    k += 1 
        
        return False
        

