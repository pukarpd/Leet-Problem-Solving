class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        if len(height) == 2: 
            return min(height) * min(height)
        

        # better code. The key : 
        left, right = 0, len(height) - 1
        res = float('-inf')

        while left < right: 
            area = min(height[left], height[right]) * (right - left)

            res = max(res, area)

            if height[left] < height[right]: 
                left += 1 
            else: 
                right -= 1 

        return res 


        # Code I wrote, 62/65 Test cases 
        # i, j = 0, len(height) - 1 
        # res = float('-inf')
        # res2 = []
        # while i < j: 
        #     area = 0
        #     if height[i] < height[j]: 
        #         area = height[i] * (j-i)
        #         i += 1 
        #     if height[j] <= height[i]: 
        #         area = height[j] * (j - i)
        #         j -= 1 
        #     res = max(res,area)
        #     res2.append(area)
        # print(res, res2)
        # return res
