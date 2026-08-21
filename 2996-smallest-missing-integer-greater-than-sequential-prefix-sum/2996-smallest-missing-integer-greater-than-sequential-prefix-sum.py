class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        # edge case if one length
        if len(nums) == 1: 
            return nums[-1] + 1 

        # edge case if the entire array is sequentially increasing
        # print(sum(nums))

        idx = 0 
        for i in range(1, len(nums)): 
            if nums[i] != nums[i-1] + 1:
                idx = i-1
                break
            if i == len(nums) - 1: 
                idx = i

        prefix = sum(nums[:idx+1])
        print(idx, nums[:idx+1])


        for i in range(prefix, math.factorial(50)): 
            if i not in nums: 
                return i 

       
    def ascend(self, arr): 
        i, j = 0, 1
        
        while i < len(arr) and j < len(arr): 
            if arr[i] >= arr[j]: 
                break 
            # print(j)
            i += 1 
            j += 1 
        j -= 1 
        # print(j)
        return True if j == (len(arr) - 1) else False



        