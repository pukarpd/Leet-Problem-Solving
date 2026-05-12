class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda nums: nums[0])
        
        heap = [intervals[0][1]]

        heapq.heapify(heap)

        for start, end in intervals[1:]: 
            if start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        
        return len(heap)



















        # find the amount of overlaps, the number of overlaps will be the number of conference rooms required. 

        # overlapped = 0 
        # first_start, first_end = intervals[0]
        # prev_end = first_end
        # for start, end in intervals[1:]: 
        #     # overlapped condition 
        #     if start < first_end: 
        #         overlapped += 1 
        #     elif prev_end > first_end: 
        #         nonoverlapped
        #     first_start, first_end = start, end 
