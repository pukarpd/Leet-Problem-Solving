class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        def dfs(i, subset, total): 
            if total == target:
                res.append(subset.copy()) 
                return
            if total > target or i == len(candidates): 
                return
            

            # include
            subset.append(candidates[i])
            dfs(i+1, subset, total+candidates[i])
            # undo
            subset.pop()

            # exclude
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]: 
                i += 1 
            dfs(i+1, subset, total) 

        dfs(0, [], 0)
        return res

          







        return res 

    


        # Implemented entire solution myself, applied backtracking concepts and problem specifications. 
        # O(n) stack frames at any given time, O(2**n recursive calls). Although the submission gave TLE, the logic is sane, accepted in neetcode. Optimal solution requires pruning search space.
        # print(candidates)

        # res = set()
        # subset = []
        # def backtrack(start, target): 
        #     # print(f"{start}\t{target}\t{subset}\t{res}")
        #     if target == 0: 
        #         res.add(tuple(sorted(subset)))
        #         return
        #     if target < 0: 
        #         return
        #     for i in range(start, len(candidates)): 
        #         subset.append(candidates[i])
        #         backtrack(i+1, target - candidates[i])
        #         subset.pop()

        # backtrack(0, target)

        # res = [list(x) for x in res]
        # return res

