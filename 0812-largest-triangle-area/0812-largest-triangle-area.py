class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        maxArea = 0 
        for i in range(len(points) - 2): 
            for j in range(i, len(points) - 1): 
                for k in range(j, len(points)): 
                    arg = [points[i], points[j], points[k]]
                    temp = self.triArea(arg)
                    maxArea = max(maxArea, temp)

        
        return maxArea

    def triArea(self, points): 

        x = [points[i][0] for i in range(len(points))]
        y = [points[i][1] for i in range(len(points))]
        
        return (1/2) * abs(x[0] * (y[1] - y[2]) + x[1] * (y[2] - y[0]) + x[2] * (y[0] - y[1]))



    # Practiced some OOP and tried a few brute force approaches, passed testcases but failed overall. There exists a closed form formula
    # and ill have to implement 
        
    #     x = [points[i][0] for i in range(len(points))]
    #     y = [points[i][1] for i in range(len(points))]

    #     base = 0
    #     indicesX = []
    #     for i in range(len(x)-1): 
    #         for j in range(i, len(x)):
    #             temp = abs((x[i] - x[j]))
    #             base = max(base, temp)
    #             if not indicesX and temp == base: 
    #                 indicesX.append([i, j])
    #             elif indicesX and temp == base:
    #                 indicesX.clear()
    #                 indicesX.append([i,j])

    #     print(indicesX)
    #     points2 = copy.deepcopy(points)
    #     points2.pop(indicesX[0][0])
    #     res1 = self.findY(points2)
    #     points2 = copy.deepcopy(points)
    #     points2.pop(indicesX[0][1])
    #     res2 = self.findY(points2)

    #     print(res1, res2, [points[indicesX[0][0]], points[indicesX[0][1]]])

    #     # res = self.triArea(points[:4])
    #     # for i in range(len(points) - 2): 
    #     #     for j in range(i, len(points) - 1): 
    #     #         for k in range(j, len(points)):
    #     #             testArr = [points[i], points[j], points[k]]
    #     #             curArea = self.triArea(testArr)
    #     #             res = max(res, curArea)
        
    #     # return res
    #     return 0.0

    # def findY(self, points): 
    #     y = [points[i][1] for i in range(len(points))]
    #     indices = []
    #     base = 0
    #     for i in range(len(y)-1): 
    #         for j in range(i, len(y)):
    #             temp = abs((y[i] - y[j]))
    #             base = max(base, temp)
    #             if not indices and temp == base: 
    #                 indices.append([i, j])
    #             elif indices and temp == base:
    #                 indices.clear()
    #                 indices.append([i,j])
    #     return [points[indices[0][0]], points[indices[0][1]]]
    # def triArea(self, points): 
        


    #     return 1/2 * base * height
