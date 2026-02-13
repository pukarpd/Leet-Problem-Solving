import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [] 
        for num in nums: 
           heapq.heappush(self.heap, num)
           if len(self.heap) > self.k:
                heapq.heappop(self.heap)      
        
        # print(self.heap)
    

    def add(self, val: int) -> int:
        # if self.heap and val < self.heap[0]: 
        #     return self.heap[0]
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)
        return self.heap[0]
        
        
        # return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)