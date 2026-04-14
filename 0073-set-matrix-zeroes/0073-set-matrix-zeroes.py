class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW, COL = len(matrix), len(matrix[0])

        seen = set()

        for r in range(ROW): 
            # visualize each outer loop
            # print(f"iteration:{r}\nmatrix:")
            # for row in matrix: 
            #     print(row)
            for c in range(COL): 
                if matrix[r][c] == 0 and (r,c) not in seen: 
                    # set zeros
                    tR = 0
                    tC = 0 
                    seen.add((r,c))
                    while tR < ROW:
                        if matrix[tR][c] != 0: 
                            matrix[tR][c] = 0 
                            seen.add((tR, c))
                        tR += 1 
                    while tC < COL: 
                        if matrix[r][tC] != 0: 
                            matrix[r][tC] = 0 
                            seen.add((r, tC))
                        tC += 1 
            
                    


