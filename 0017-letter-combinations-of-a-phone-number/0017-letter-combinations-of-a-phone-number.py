class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        n_map = {i:[] for i in range(2,10)}

        j = 97
        rv = 3 
        for i in range(2,10):
            rv = 4 if i == 7 or i == 9 else 3
            for k in range(rv): 
                n_map[i].append(chr(j))
                j += 1 
       
        res = []
        def backtrack(index, substring):
            if index == len(digits): 
                res.append(''.join(substring))
                return 
            letters = n_map[int(digits[index])]
            for letter in letters: 
                substring.append(letter)
                backtrack(index + 1, substring)
                substring.pop()
            return
    
        backtrack(0, [])
        return res

