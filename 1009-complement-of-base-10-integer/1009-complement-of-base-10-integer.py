class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: 
            return 1
        k = n.bit_length()
        mask = (1<<k)-1
        return n ^ mask