class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        atot = sum(aliceSizes)
        btot = sum(bobSizes)

        a = set(aliceSizes)
        b = set(bobSizes)
  
        res = []
        for k in a: 
            for k2 in b: 
                if atot - k + k2 == btot - k2 + k: 
                    return [k, k2]



