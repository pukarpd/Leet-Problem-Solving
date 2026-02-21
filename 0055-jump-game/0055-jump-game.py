class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # tracking the idx that we can reach maximally 
        maxReach = 0

        for i in range(len(nums)): 
            if i > maxReach: 
                return False 
            maxReach = max(maxReach, i + nums[i])

            
        
        return True 



        # O(n * n) solution, didnt work. Learning neetcode soln now. 
        # if not nums or len(nums) == 1: 
        #     return True 
        # if len(nums) == 2 and nums[0] >= 1: 
        #     return True

        
        # # dp = [False] * (len(nums) - 1)
        
        # # O(n)
        # res = False
        # j = 0 
        # for i in range(len(nums) - 2): 
        #     j = i 
        #     while j < len(nums) - 1:
        #         # storing prev index
        #         k = j 
        #         j = nums[j] + k 
        #         # print(i, k, j)
        #         # break conditions 
                
        #         if j >= (len(nums) - 1): 
        #             # dp[i] = True 
        #             res = True 
        #             break
        #         if nums[j] == 0: 
        #             # dp[i] = False
        #             break
        #         # jump logic
        # # print(dp)
        # return res 


                

        
