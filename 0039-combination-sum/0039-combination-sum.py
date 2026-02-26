class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, subset = [], []
        def backtrack(start, target):
            # print(f"{start}\t{ target}\t{subset}\t{res}")
            if target == 0: 
                res.append(subset.copy())

            if target < 0: 
                return  
            
            
           
            for i in range(start, len(candidates)): 
                subset.append(candidates[i])
                new_target = target - candidates[i]
                backtrack(i, new_target) #reuse allowed 
                subset.pop()
                # backtrack(i+1, target)
                


        backtrack(0, target)
        return res