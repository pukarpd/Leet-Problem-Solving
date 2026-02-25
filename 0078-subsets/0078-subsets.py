class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        self.res = [] 

        def backtrack (start, path): 
            
            self.res.append(path.copy())
            # print(start,'\t---',path,'\t\t---',self.res)

            for i in range(start, len(nums)): 
                path.append(nums[i])
                # print(f"**{path}**")
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])
        return self.res


        