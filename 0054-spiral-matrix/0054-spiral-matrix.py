class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # testcase = []
        # l, o = 1, 6
        # for i in range(1, 6): 
        #     temp = [] 
        #     for i in range(l, o): 
        #         temp.append(i)
        #     l += 5 
        #     o += 5
        #     testcase.append(temp)
        # print(testcase)

        ROW, COL = len(matrix) , len(matrix[0])
        TOTAL = ROW * COL

        left, right = 0, COL - 1
        top, bottom = 0, ROW - 1 


        #go to the right
        res = []

        while len(res) < TOTAL:

            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            if top > bottom: break

            # Top to Bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right: break

            # Right to Left
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
            if top > bottom: break

            # Bottom to Top
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right: break
            
        return res

        