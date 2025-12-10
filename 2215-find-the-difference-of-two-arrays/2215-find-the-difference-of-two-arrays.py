class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        unique1 = set(nums1)
        unique2 = set(nums2)
        # print(unique1, unique2)

        output = []
        res = []
        for num in unique1: 
            
            if num not in unique2:
                res.append(num)
        output.append(res)
        res = []
        for num in unique2: 
            if num not in unique1: 
                res.append(num)

        output.append(res)

        return output 

