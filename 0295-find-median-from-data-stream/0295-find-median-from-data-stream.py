class MedianFinder: 

    def __init__(self):
        # stores the left portion of the sorted array, and one extra element if len(total) is odd
        self.left_maxHeap = []
        # stores the right portion of the sorted Array 
        self.right_minHeap = []
        heapq.heapify(self.left_maxHeap)

        heapq.heapify(self.right_minHeap)
        
    def addNum(self, num: int) -> None:

        if not self.left_maxHeap or num <= -self.left_maxHeap[0]: 
            heapq.heappush(self.left_maxHeap, -num)
        else: 
            heapq.heappush(self.right_minHeap, num)


        if len(self.left_maxHeap) > len(self.right_minHeap) + 1: 
            val = -heapq.heappop(self.left_maxHeap)
            heapq.heappush(self.right_minHeap, val)
        elif len(self.right_minHeap) > len(self.left_maxHeap): 
            val = heapq.heappop(self.right_minHeap)
            heapq.heappush(self.left_maxHeap, -val)


    def findMedian(self) -> float: 
        if len(self.left_maxHeap) > len(self.right_minHeap):
            return -self.left_maxHeap[0]

        return (-self.left_maxHeap[0] + self.right_minHeap[0]) / 2   



    # def __init__(self):

    #     # left part of the stream
    #     self.maxHeap = [] 
    #     # right part of the stream
    #     self.minHeap = []
        
    #     heapq.heapify(self.minHeap)
    #     heapq.heapify(self.maxHeap)

    #     self.median = None 

    # def addNum(self, num:int) -> None: 
    #     heapq.heappush(self.maxHeap, -num)

    #     self.findMedian()

        
    #     # need to balance both heaps: 
    #     difference = abs(len(self.minHeap) - len(self.maxHeap))

    #     larger_heap = self.maxHeap if len(self.maxHeap) > len(self.minHeap) else self.minHeap
    #     smaller_heap = self.maxHeap if len(self.maxHeap) < len(self.minHeap) else self.minHeap

    #     # there was a while here
            
    #     # print(self.maxHeap, self.minHeap, self.median)

    # def findMedian(self) -> float: 

    #     # if self.minHeap and not self.maxHeap: 
    #     #     self.median = self.minHeap[0]
    #     #     return self.median
    #     if self.maxHeap and not self.minHeap: 
    #         self.median = -self.maxHeap[0] 
    #         return self.median


    #     lengths_of_heaps = len(self.maxHeap) + len(self.minHeap)

    #     if lengths_of_heaps % 2 == 0: 
    #         self.median = (-self.maxHeap[0] + self.minHeap[0]) / 2 
    #     else: 
    #         larger_heap = self.maxHeap if len(self.maxHeap) > len(self.minHeap) else self.minHeap
    #         if larger_heap[0] <= 0:
    #             self.median = -larger_heap[0]
    #         else: 
    #             self.median = larger_heap[0] 

    #     return self.median

    # def balance_heaps(self, heap1, heap2): 



    # brute force O(nlogn) solution using heaps
    # def __init__(self):
    #     self.initialHeap = []
    #     heapq.heapify(self.initialHeap)

    #     self.maxHeap = []
    #     heapq.heapify(self.maxHeap)    

    # def addNum(self, num: int) -> None:
    #     heapq.heappush(self.initialHeap, num)


    # def findMedian(self) -> float:
    #     popThis = (len(self.initialHeap) // 2)
    #     if len(self.initialHeap) % 2 == 1: 
            
    #         temp = []
    #         for i in range(popThis): 
    #             val = heapq.heappop(self.initialHeap)
    #             temp.append(val)
    #         val = heapq.heappop(self.initialHeap)
    #         temp.append(val)
    #         for v in temp: 
    #             heapq.heappush(self.initialHeap, v)
    #         return val 

    #     if len(self.initialHeap) % 2 == 0: 
    #         popThis = (len(self.initialHeap) // 2)
    #         temp = []
    #         for i in range(popThis): 
    #             val = heapq.heappop(self.initialHeap)
    #             temp.append(val)
    #         for val in temp: 
    #             heapq.heappush(self.maxHeap, -val)
    #         midmin = heapq.heappop(self.initialHeap)
    #         midmax = heapq.heappop(self.maxHeap)

    #         heapq.heappush(self.initialHeap, midmin)
    #         heapq.heappush(self.maxHeap, midmax)

    #         for val in self.maxHeap: 
    #             heapq.heappush(self.initialHeap, -val)

    #         self.maxHeap = []
            
    #         return (midmin + -midmax) / 2




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()