class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)

        i = 0 
        
        while i < len(nums):
            minKey = min([k for k in counter.keys()])
            if counter[minKey] > 0: 
                nums[i] = minKey
                counter[minKey] -= 1
                i += 1
            if counter[minKey] == 0: 
                del counter[minKey]
             
         



