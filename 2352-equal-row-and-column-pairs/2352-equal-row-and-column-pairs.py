class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        newGrid = []
        for col in range(COLS-1,-1,-1):
            newRow = []
            for row in range(ROWS): 
                newRow.append(grid[row][col])
            newGrid.append(newRow)
        res = 0 
        for g2 in newGrid:
            # print(g2)
            for g1 in grid: 
                if g2 == g1: 
                    res += 1 
                
        return res
        