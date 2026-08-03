class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # max first, min next vs min first, max next

        mif, mas = float("inf"), float("-inf")
        idx = 0 

        for i, arr in enumerate(arrays): 
            if arr[0] < mif: 
                mif = arr[0]
                idx = i 
        for i, arr in enumerate(arrays): 
            if idx != i and arr[-1] > mas: 
                mas = max(mas, arr[-1])

        # max first
        mis, maf = float("inf"), float("-inf")

        for i, arr in enumerate(arrays): 
            if arr[-1] > maf: 
                maf = arr[-1]
                idx = i 


        for i, arr in enumerate(arrays): 
            if i != idx and arr[0] < mis: 
                mis = arr[0]

        # print(mif, mas, mis, maf)


        return max((abs(mas - mif)), (abs(maf - mis)))
