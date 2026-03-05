class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1: 
            return 0

        s_arr = [d for d in s]

        s_arr_count = 0 
        # Loop through original
      
        i, j = 0, 1

        while j < len(s_arr): 
            # print(f"{s_arr[i]}\t{s_arr[j]}\t{s_arr}")
            if s_arr[i] == '1' and s_arr[j] == '1': 
                s_arr[j] = '0'
                s_arr_count += 1 
            elif s_arr[i] == '0' and s_arr[j] == '0': 
                s_arr[j] = '1'
                s_arr_count += 1 
            i+= 1 
            j += 1 

        return min(s_arr_count, len(s) - s_arr_count)


        


        # first instinct that passes test cases, problem was much simpler than this, start with either 0 or 1 and take min,. 
        # s1 = [s[i] for i in range(len(s)) if i % 2 == 0] #Even
        # s2 = [s[i] for i in range(len(s)) if i % 2 == 1] #Odd
        
        # pairs = defaultdict(int)
        # for e, j in zip(s2, s1): #form pairs
        #     pairs[(e,j)] += 1 
        
        # # print(pairs)
        # res = 0 
        # for k, v in pairs.items(): 
        #     if k == ("0","0") or k == ("1","1"): 
        #         res += v

        # return res 

       