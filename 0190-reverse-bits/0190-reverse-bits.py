class Solution:
    def reverseBits(self, n: int) -> int:
        
        padding = ''.join(['0'] * (32 - len(bin(n)[2:])))
        new_bin = (padding + (bin(n)[2:]))
        return int(new_bin[::-1], 2)