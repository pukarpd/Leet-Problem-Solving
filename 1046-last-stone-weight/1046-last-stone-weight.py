class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # edge case 
        if len(stones) == 1:
            return stones[0]

        # max heap algorithm, implemented myself
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        # print(max_heap)
        # print(max_heap)
        while len(max_heap) != 1:
            largest = -heapq.heappop(max_heap)
            # print(max_heap, "\n",largest)
            # print(largest)
            if max_heap: 
                slargest = -heapq.heappop(max_heap)
            else: 
                slargest = 0 
            # print(max_heap,"\n",slargest)
            this = largest - slargest
            # print(this)
            heapq.heappush(max_heap, - this) 

        return -max_heap[0]
