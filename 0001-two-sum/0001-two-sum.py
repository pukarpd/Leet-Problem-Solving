class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_set = {}

        for i, n in enumerate(nums):  
            if (target - n) in nums_set: 
                return [i, nums_set[target-n]]
            else:
                nums_set[n] = i  

        return []

