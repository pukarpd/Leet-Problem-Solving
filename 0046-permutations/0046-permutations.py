class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # O(n)stack frames so space O(2**n) time for 2**n recursion calls to find all permutations 
        res, subset = [], [] 
        def backtrack(index, used, subset): 
            # print(f"{index}\t{used}\t{subset}\t{res}")
            if len(subset) == len(nums): 
                res.append(subset[:])
                return

            for i in range(len(nums)): 
                
                if nums[i] in used: 
                    continue 
                subset.append(nums[i])
                used.add(nums[i])
                backtrack(i+1, used, subset)
                this = subset.pop()
                used.remove(this)

        
        backtrack(0,set(), [])

        return res
