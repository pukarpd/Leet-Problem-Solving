class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curSum = [0] * (len(nums) + 1)
        maxSum = float("-inf")
        for i in range(len(nums)): 
            if curSum[i] >= 0: 
                curSum[i+1] = curSum[i] + nums[i]

            else:
                curSum[i+1] = nums[i]
            maxSum = max(curSum[i+1], maxSum)


        return maxSum
