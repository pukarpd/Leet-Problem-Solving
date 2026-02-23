class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # same approach but inverted solution. Just adds everything and checks      combinations later lol 
        seen = set()

        i, j = 0, k - 1 

        while j < len(s): 
            if s[i:j+1] not in seen: 
                seen.add(s[i:j+1])
            i += 1 
            j += 1 

        return len(seen) == 2**k

        # This has to be the first algorithm i wrote thats O(2^k) first exponential time 
        # complexity algo lol super slow  
        # mySet = set()
        # bit_k = "0" * k
        # # print(bit_k)
        # for i in range(2**len(bit_k)):
        #     width = len(bin(k)[2:]) - len(bin(i)[2:])
        #     val = bin(i)[2:]
        #     val = ("0" * width) + val
        #     mySet.add(val)

       

        # i, j = 0, len(bit_k) - 1 
        # res = 0
        # while j < len(s): 
        #     if s[i:j+1] in mySet: 
        #         mySet.remove(s[i:j+1])
        #     i += 1  
        #     j += 1 

        
        # return False if mySet else True
