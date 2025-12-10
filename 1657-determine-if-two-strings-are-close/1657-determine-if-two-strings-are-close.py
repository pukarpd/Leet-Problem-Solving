class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        k1 = [key for key in c1.keys()]
        k2 = [key for key in c2.keys()]
        v1 = [val for val in c1.values()]
        v2 = [val for val in c2.values()]
        k1.sort()
        k2.sort()
        v1.sort()
        v2.sort()

        if k1 == k2 and v1 == v2: 
            return True 
        return False