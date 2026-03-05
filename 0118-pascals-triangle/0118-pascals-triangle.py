class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascals = []
        for i in range(numRows): 
            temp = []
            for j in range(i+1): 
                temp.append(1)
            pascals.append(temp)

        for i in range(2, numRows): 
            curRow = pascals[i]
            print(pascals)
            for j in range(1, len(curRow) - 1): 
                pascals[i][j] = pascals[i-1][j-1] + pascals[i-1][j]

        return pascals