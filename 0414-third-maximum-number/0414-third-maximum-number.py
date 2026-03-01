class Solution:
    def thirdMax(self, nums: List[int]) -> int:


        # deduplicate and prep data O(1)
        numSet = set(nums)
        nums2 = [-v for v in numSet]

        # data structure that always holds maxVal at idx0 O(n) build, O(logn) pop 
        heapq.heapify(nums2)
        maxVal = 0
        length = len(nums2)

        # pop 3 times, if available, else return max 
        for i in range(3): 
            if length >= 3:
                maxVal = -heapq.heappop(nums2)
            else: 
                maxVal = -nums2[0]
                break
        
        return maxVal