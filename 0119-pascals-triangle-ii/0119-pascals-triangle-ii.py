class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        pascals = [] 

        for i in range(rowIndex + 1): 
            temp = []
            for j in range(i+1): 
                temp.append(1)
            pascals.append(temp)

        for i in range(2, rowIndex+1):
            curRow = pascals[i]
            for j in range(1, len(curRow)-1): 
                pascals[i][j] = pascals[i-1][j-1] + pascals[i-1][j]

        return pascals[rowIndex] 

