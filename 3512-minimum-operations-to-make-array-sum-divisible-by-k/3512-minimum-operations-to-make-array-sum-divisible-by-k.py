class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        minDiv = 0 
        tracker = [0] * len(nums)

        for i in range(len(nums)):  
            while sum(nums) % k != 0: 
                if nums[i] == 0:
                    break
                nums[i] -= 1
                minDiv += 1 
            tracker[i] = minDiv
            minDiv = 0 
    
        if sum(nums) == 0 or sum(tracker) < k:
            return sum(tracker)
        else: 
            return min(tracker)

        