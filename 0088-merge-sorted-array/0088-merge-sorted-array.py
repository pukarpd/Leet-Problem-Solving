class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0 
        j = 0 

        smallerVal = min(m, n)
        while i <  smallerVal and j < smallerVal:
            if nums1[i] > nums2[j]: 
                nums1[i], nums2[j] = nums2[j], nums1[i]
                i += 1
                j += 1 
            else: 
                i += 1 
        rest = 0 
        # if i == m: 
        while rest < n: 
            nums1[i] = nums2[rest]
            i += 1 
            rest += 1 


