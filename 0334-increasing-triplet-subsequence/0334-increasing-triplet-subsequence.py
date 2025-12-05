class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) == 1 or len(nums) == 2: 
            return False 

        if len(nums) == 3: 
            return True if nums[0] < nums[1] and nums[1] < nums[2] else False
        
        first = float('inf')
        second = float('inf')

        for num in nums: 
            if num <= first:
                first = num
                continue 
            if num <= second: 
                second = num
                continue 
            if num > first and num > second:
                return True 
        return False

        # #flawed attempt
        # while i < len(nums) - 2 and k < len(nums): 
        #     print(i,j,k)
        #     if nums[i] < nums[j] and nums[j] < nums[k]: 
        #         return True
        #     elif nums[i] > nums[j]: 
        #         i += 1 
        #         j = i + 1 
        #         k = j + 1 
        #     if nums[i] < nums[j]:
        #         while nums[j] > nums[k] and k < len(nums): 
        #             print(j,k)
        #             k += 1 

        
        # return False
        

