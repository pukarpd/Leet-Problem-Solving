class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0 
        nums.sort()

        i, j = 0, len(nums) - 1

        while i < j: 
            possibleK = nums[i] + nums[j]
            print(possibleK, i, j)
            if possibleK == k: 
                res += 1 
                i += 1 
                j -= 1 
            if possibleK < k: 
                i += 1 
            if possibleK > k: 
                j -= 1 
        
       

        return res

         


       
