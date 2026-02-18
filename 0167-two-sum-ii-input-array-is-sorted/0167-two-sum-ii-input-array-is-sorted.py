class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers 
        l , r = 0, len(nums) - 1 
        res = []
        while l < r: 
            num = nums[l] + nums[r]
            if num > target: 
                r -= 1 
            elif num < target: 
                l += 1 
            else: 
                res.append(l+1)
                res.append(r+1)
                break
        return res