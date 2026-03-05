class Solution:
    def numDecodings(self, s: str) -> int:
        # dont need 
        # e = [i for i in range(1,27)]
        # d = [chr(i).upper() for i in range(97,123)]

        # # print(e,d)
        # mapping = {}
        # for en, dc in zip(e, d): 
        #     mapping[en] = dc
        # print(mapping)
        @cache
        def dfs(i): 
            if i == len(s): 
                return 1 
            if s[i] == '0': 
                return 0

            res = dfs(i+1)
            if (i + 1 < len(s) and 
               (s[i] == '1' or s[i] == '2' and s[i + 1] in "0123456")):
               res += dfs(i+2)
            return res

        return dfs(0)