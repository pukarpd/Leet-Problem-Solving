class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = strs[0]

        for i in range(1,len(strs)):
            j, k = 0, 0 
            commonPrefix = ''
            while j < min(len(strs[i]), len(res)):
                if res[j] == strs[i][j]:
                    commonPrefix += strs[i][j]
                elif res[j] != strs[i][j]:  
                    break
                j+= 1
                k += 1 
            res = commonPrefix

        return res 


