class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixAndSuffix(str1, str2): 
            
            if len(str1) > len(str2): 
                return 0

            longe, short = str2, str1
            front = longe[:len(short):]
            
            longer = list(longe)
            longer = longer[::-1]
            longer = longer[:len(short):]
            longer = longer [::-1]
            longer = ''.join(longer)

            back = longer
            # print(longer,short)
            # print(front, back)
            # print(str1 == front, str1 == back)
            if str1 == front and str1 == back: 
                return 1
            else:
                return 0

        res = 0
        
        i = 0 
        j = 1
        while i < len(words): 
            while j < len(words):
                temp = isPrefixAndSuffix(words[i], words[j])
                # print(temp)
                j += 1
                res += temp 
            i += 1 
            j = i + 1 

        return res