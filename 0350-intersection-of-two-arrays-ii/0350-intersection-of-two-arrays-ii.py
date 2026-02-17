class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for num in nums1: 
            map1[num] += 1 
        for num in nums2: 
            map2[num] += 1 

        res = []
        
        for k, v in map1.items(): 
            multiplier = min(v, map2[k]) 
            for i in range(multiplier): 
                res.append(k)
    
        return res