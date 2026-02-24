class Solution:
    def jump(self, nums: List[int]) -> int:
        
        current_end = 0 
        farthest = 0 
        jumps = 0 
        # greedy approach
        for i in range(len(nums) - 1): 
            farthest = max(farthest, i + nums[i])

            if i == current_end: 
                jumps += 1 
                current_end = farthest

        return jumps


        # O(n**2) greedy solution, but wrong approach. there has to be a better way. 
        # res = 0 
        # i = 0
        # while i < len(nums) - 1: 
        #     # take a look at all the children, select the maximum child. 
        #     found_IDX = 0 
        #     greedy_child = 0 
        #     for j in range(nums[i]+1):
        #         child = min(j + i, len(nums) - 1) 
        #         greedy_child = max(greedy_child, nums[child])
        #         if nums[child] == greedy_child: 
        #             found_IDX = child
        #     res += 1 
            
        #     i = found_IDX 
        #     # print(greedy_child)
        # testCase = [i for i in range(1000-1, -1, -1)]
        # print(testCase)

        # return res



            
