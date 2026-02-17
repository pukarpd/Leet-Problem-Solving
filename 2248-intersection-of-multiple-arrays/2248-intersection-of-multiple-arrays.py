class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        mapa = defaultdict(int)

        for num in nums: 
            for i in num: 
                mapa[i] += 1 
        res = []
        for k, v in mapa.items(): 
            if v == len(nums): 
                res.append(k)

        res.sort()

        return res
        