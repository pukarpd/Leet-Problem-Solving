class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        if len(chars) == 1: 
            return 1 
        i = 1
        j = 0
        while j < len(chars) - 1 and i < len(chars):  
            while i < len(chars) and chars[i] == chars[j]:
                print(i)
                i += 1 
            length = i - j 
            if length == 1: 
                s += chars[j] 
            else: 
                s += chars[j]
                s += str(length)
            j = i 
            i += 1
        if chars[-2] != chars[-1]: 
            s += chars[-1] 
        print(s)
        for i in range(len(chars)): 
            chars.pop()
        
        for i in range(len(s)): 
            chars.append(s[i])

        print(chars)

        
        
            

            
             
            

