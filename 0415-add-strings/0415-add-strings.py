class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        hashmap = {}
        BASESTRING = "0123456789"

        
        for i in range(0, 10):
            hashmap[BASESTRING[i]] = i
        print(hashmap)

        if len(num1) == 1 and len(num2) == 1: 
            return str(hashmap[num1[0]] + hashmap[num2[0]])

        
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        longe = list(num2)
        short = list(num1)
        # print(longe, short)
        longe = longe[::-1]
        short = short[::-1]
        remainder = len(longe) - len(short)
        for i in range(remainder): 
            short.append('0')
        print(longe, "\n", short)

        REM = len(short)
        res = []
        carry = 0
        for i in range(len(longe)):
                addition = hashmap[longe[i]] + hashmap[short[i]] + carry
                digits = str(addition)
                print(digits)
                if len(digits) > 1:
                    res.append(int(digits[1]))
                    carry = int(digits[0])
                    # print(carry)
                else:
                    carry = 0
                    res.append(addition) 
        
        if carry > 0: 
            res.append(carry)
        ren = ''
        for i in range(len(res)-1, -1, -1): 
            ren += str(res[i]) 
        
        # print(res, ren)

        return ren

            

            
    
                
        
