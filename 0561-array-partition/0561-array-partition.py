class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0 
        i, j = 0, 1 
        while j < len(nums): 
            res += min(nums[i], nums[j])
            i += 2
            j += 2 
        return res
