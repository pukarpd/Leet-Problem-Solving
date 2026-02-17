class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Neetcode
        res = []
        # newStart, newEnd = copy.deepcopy(newInterval[0]), copy.deepcopy(newInterval[1])
        for i, (start,end) in enumerate(intervals): 
            if newInterval[1] < start: 
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > end: 
                res.append(intervals[i])
            else: 
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        res.append(newInterval)
        return res
        


        # first attempt without looking at any neetcode, solved 2 intervals blind before this.
        # I think doing binary search here was a mistake. In stead of solving in O(logn) I should have
        # determined overlap, appended to res accordingly. 
        # left, right = 0, len(intervals) - 1 
        # target = newInterval[0]
        # while left <= right: 
        #     mid = (left + right) // 2 
        #     comp = intervals[mid][0]
        #     if comp < target:
        #         left = mid + 1 
        #     else:
        #         right = mid - 1 

        # if right == len(intervals) - 1: 
        #     res = intervals
        #     res.append(newInterval)
        #     print(res)
        #     return res

        # if right < 0: 
        #     right += 1 

        # newStart, newEnd = newInterval[0], newInterval[1]
        # mergeIdx = 0

        # for i, (s,e) in enumerate(intervals): 
        #     if s <= newEnd and e >= newEnd:
        #         mergeIdx = i 
        #         break 
    
        # res1 = intervals[:right]
        # res2 = intervals[mergeIdx+1:] 
        # needsMerging = intervals[right:mergeIdx+1]
        # print(res1, needsMerging, res2)
        # merged = [[newStart, newEnd]] 
        # merged[0][0] = min(intervals[right][0], newStart)
        # merged[0][1] = max(intervals[mergeIdx][1], newEnd)

        # return res1 + merged + res2





             
        