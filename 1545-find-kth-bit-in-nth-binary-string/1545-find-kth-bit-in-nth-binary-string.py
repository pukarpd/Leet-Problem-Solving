class Solution:
    def findKthBit(self, n: int, k: int) -> str: 
        # the naiive approach would be to write a straightforward O(n**3) 
        # print(bin(1)[2:],"There is One 2**0")
        res = self.invert(bin(1)[2:])
        # track the indices where we 

        for i in range(2, n+1): 

            # print(f"Initial:{res}\tAppended One: {"1"}\nOld res reversed:{self.invert(res[::-1])}")
            res = (res + "1" + self.invert(res[::-1]))
            # print(res)
        
        return res[k-1]
        # if n % 2 == 0: 
        #     return res[k-1]
        # elif res[k-1] == '1': 
        #     return '0' 
        # else:
        #     return '1'

    def invert(self, string): 
        string = [l for l in string]
        # print(string)
        for s in range(len(string)): 
            if string[s] == '1': 
                string[s] = "0"
            else: 
                string[s] = "1"

        return ''.join(string)
