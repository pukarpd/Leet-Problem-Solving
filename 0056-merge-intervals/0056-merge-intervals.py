class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        # sort by start value

        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]
        # print(intervals)
        for start, end in intervals[1:]: 
            # print(output, start, end)
            lastEnd = output[-1][1]
            # print(lastEnd)
            if start <= lastEnd: 
                output[-1][1] = max(lastEnd, end)
            else: 
                output.append([start, end])
            # [1,5] , [2,4] we want to keep the 5m thats why the last end vs end merging. 
        return output
        # # my method
        # new = [] 
        # for i in intervals: 
        #     new.append(i[0])
        # zipped_intervals = sorted(zip(intervals, new))

        # new_intervals = [item[0] for item in zipped_intervals] 
        # print(new_intervals)

























        # sorter = []
        # for arr in intervals: 
        #     suma = sum(arr)
        #     sorter.append(suma)
        
        # news = sorted(zip(sorter, intervals))
        # new = [item[1] for item in news]
        

        # left = 0 
        # right = 1
        # res = []
        # for i in range(len(new)):
        #     while right < ROWS: 
        #         num1 = new[left][1]
        #         num2 = new[right][0]
        #         if num1 >= num2:
        #             newarr = [item for item in new[left]]
        #             for item in new[right]: 
        #                 newarr.append(item)
        #             print(newarr)
        #             res.append([min(newarr), max(newarr)])
        #             left += 2 
        #             right += 2
        #         else: 
        #             res.append(new[left])
        #             left += 1 
        #             right += 1 
        #         new = res
        #         left = 0 
        #         right = 1

        # if right == len(new): 
        #     res.append(new[right -1 ])
        # print(new, res)

        # return res
        



