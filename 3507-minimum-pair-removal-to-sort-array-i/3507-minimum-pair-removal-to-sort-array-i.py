class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if nums == sorted(nums): 
            return 0
        nums2 = copy.deepcopy(nums)
        arr = [] 
        res = 0

        while True:
            nums3 = sorted(nums2)
            if nums3 == nums2: 
                break
            i, j = 0, 1 
            while j < len(nums2):
                val = (nums2[i] + nums2[j], i)
                arr.append(val)
                i+=1 
                j+=1 
            heapq.heapify(arr)
            if not arr:
                break
            val = heapq.heappop(arr)
            one_idx, two_idx = val[1], val[1] + 1
            nums2[one_idx] = val[0]
            nums2.pop(two_idx)
            arr = []
            res += 1 
        
        return res 
         
            
