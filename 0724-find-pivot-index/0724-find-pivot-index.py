class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumleft = [0] * len(nums)
        sumright = [0] * len(nums)
        ls, rs = 0, 0
        for i in range(len(nums)):
            ls += nums[i]
            sumleft[i] = ls

        for i in range(len(nums)-1, -1, -1): 
            rs += nums[i]
            sumright[i] = rs
        # sumright.reverse()
        print(sumleft,"\n",sumright)

        for i in range(len(nums)): 
            if sumleft[i] == sumright[i]: 
                return i
        

        return -1


        # print(prefix)