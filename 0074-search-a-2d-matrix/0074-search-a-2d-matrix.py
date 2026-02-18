class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        largeArr = [] 
        for arr in matrix: 
            largeArr += arr 


        left = 0 
        right = len(largeArr) -1 

        while left <= right: 
            mid = (left + right) // 2 
            if largeArr[mid] > target: 
                # shrink right
                right = mid - 1
            elif largeArr[mid] < target: 
                left = mid + 1 
            elif largeArr[mid] == target: 
                return True 
            else: 
                return False

            