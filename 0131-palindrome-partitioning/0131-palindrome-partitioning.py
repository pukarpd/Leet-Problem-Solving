class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = [] 
        def backtrack(start, substring): 
            if len(s) == sum([len(s) for s in substring]): 
                res.append(substring[:])
                return

            for end in range(start+1, len(s) + 1): 
                sub = s[start:end]

                if sub == sub[::-1]: 
                    substring.append(sub)
                    backtrack(end, substring)
                    substring.pop()

    
        backtrack(0, [])
        return res