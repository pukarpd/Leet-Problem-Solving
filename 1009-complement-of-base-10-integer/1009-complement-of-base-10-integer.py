class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = int(''.join(['1'] * len(bin(n)[2:])), 2)
        return n ^ mask