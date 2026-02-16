class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
        intervals.sort(key = lambda i : i[0], reverse = True)

        # print(intervals)
        res = [] 
        res.append(intervals.pop())
        for i in range(len(intervals)-1,-1,-1):
            temp = intervals[i] 
            # print(res, temp)
            if res[-1][1] >= temp[0]: 
                res[-1][1] = max(temp[1], res[-1][1])
            else: 
                res.append(temp)
        
        return res[::-1]

        # i, j = 0 , 1: 
