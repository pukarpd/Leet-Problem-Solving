class Solution:
    def reverseBits(self, n: int) -> int:
        res =  0
        for i in range(32): 
            bit = (n>>i) & 1            # we take the last bit
            res = res | (bit << (31 - i))
        return res 
        # padding = ''.join(['0'] * (32 - len(bin(n)[2:])))
        # new_bin = (padding + (bin(n)[2:]))
        # return int(new_bin[::-1], 2)