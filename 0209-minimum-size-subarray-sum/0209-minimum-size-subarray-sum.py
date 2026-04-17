class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        i =  0 
        window_sum = 0 

        for j in range(len(nums)): 
            window_sum += nums[j]

            while window_sum >= target: 
                res = min(len(nums[i:j+1]), res)
                window_sum -= nums[i]
                i += 1 

        return res if res != float('inf') else 0 