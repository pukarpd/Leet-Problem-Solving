class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res, subset = set(), []

        # no pruning since constraints are small. 
        def backtrack(start):
            res.add(tuple(sorted(subset).copy()))

            for i in range(start, len(nums)): 
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()


        backtrack(0)
        return [list(x) for x in res]