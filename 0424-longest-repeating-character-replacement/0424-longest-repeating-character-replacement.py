class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1: 
            return 1 
        

        freq = {}
        res = 0
        i, j = 0, 1
        freq[s[i]] = 1 
        while i < j and j < len(s): 
            if s[j] not in freq: 
                freq[s[j]] = 1 
            else: 
                freq[s[j]] += 1 
            maxFreq = max(freq.values())
            diff = (j - i + 1) - maxFreq
            print(maxFreq, diff)
            if diff > k: 
                freq[s[i]] -= 1 
                i += 1 
            res = max(res, len(s[i:j+1]))
            j += 1 
        return res

        # freq = {}
        # res = 0
        # i = 0

        # for j in range(len(s)):
        #     freq[s[j]] = freq.get(s[j], 0) + 1
            
        #     maxFreq = max(freq.values())
            
        #     while (j - i + 1) - maxFreq > k:
        #         freq[s[i]] -= 1
        #         i += 1
            
        #     res = max(res, j - i + 1)

        # return res







            

