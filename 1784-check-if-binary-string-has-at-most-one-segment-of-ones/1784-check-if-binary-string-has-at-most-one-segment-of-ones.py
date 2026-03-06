# what does contiguous segment mean? 
# not just 11. i need to test. 

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # set check 
    
        if s.count("1") == 1: 
            return True
    
        i, j = 0, 1 
        first_ones = False
        found_zero = False 
   

        while j < len(s): 
            #  Case 1: we found a contiguous ones
            # print(f"l:{i, s[i]}\tr:{j, s[j]}\tfirst:{first_ones}\tzero:{found_zero}")
            if not found_zero and s[i] ==  '1' and s[j] == '1': 
                first_ones = True 
                j += 1 
            elif found_zero and first_ones and s[i] == '1' or s[j] == '1': 
                return False
            else: 
                found_zero = True
                i = j 
                j += 1 
            
            

             
        return first_ones 