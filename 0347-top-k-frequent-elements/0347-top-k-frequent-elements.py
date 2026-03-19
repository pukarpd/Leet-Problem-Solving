class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_freq = k
        c = Counter(nums)
        res = []
        for k, v in c.items(): 
            curmax = max(c.values())
            if v == curmax and k_freq > 0: 
                res.append(k)
                c[k] = 0
                k_freq -= 1 
        return res
