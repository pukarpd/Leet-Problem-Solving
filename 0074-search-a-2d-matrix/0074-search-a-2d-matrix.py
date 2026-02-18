class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        foundROW = 0 

        top, down = 0, len(matrix) - 1
        foundRow = None
        while  top <= down: 
            mid = (top + down) // 2
            if matrix[mid][0] < target and matrix[mid][-1] < target: 
                top = mid + 1  
            elif matrix[mid][0] > target and matrix[mid][-1] > target: 
                down = mid - 1 
            else: 
                foundRow = mid
                break
        print(foundRow)
        if foundRow == None: 
            return False
        l, r  = 0, len(matrix[0]) - 1 
        print(l, r)
        foundVal = False
        while l <= r: 
            mid = (l + r) // 2 
            print(mid)
            if matrix[foundRow][mid] < target: 
                l = mid + 1 
            elif matrix[foundRow][mid] > target: 
                r = mid - 1 
            else: 

                foundVal = True 
                break 
        
        return foundVal

        


