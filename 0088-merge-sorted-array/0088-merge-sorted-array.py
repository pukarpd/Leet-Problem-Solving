class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m 
        rest = 0 
        while i < n+m: 
            nums1[i] = nums2[rest]
            i+=1
            rest+=1
        print(nums1)
        nums1.sort()