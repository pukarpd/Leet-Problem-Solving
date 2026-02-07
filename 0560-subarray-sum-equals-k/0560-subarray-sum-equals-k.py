class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        cursum = 0 
        hashmap = {0:1}

        for n in nums: 
            cursum += n 
            diff = cursum - k 

            res += hashmap.get(diff, 0)

            hashmap[cursum] = 1 + hashmap.get(cursum, 0)
        
        return res



        # for i in range(len(nums)):





        # # O(n^2) solution
        # res = 0 
        # for i in range(len(nums)): 
        #     for j in range(i, len(nums)): 
        #         if sum(nums[i:j+1])== k: 
        #             res += 1 
        
        # return res