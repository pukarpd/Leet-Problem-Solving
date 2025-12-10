class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1 
        res = 0 
        left = 0

        for right in range(len(nums)): 

            if nums[right] == 0: 
                k -= 1 
            if k < 0 : 
                if nums[left] == 0:
                    k += 1 
                left+=1
            # print(nums[left:right+1])
            res = max(res, len(nums[left:right+1])-1)
        return res
                