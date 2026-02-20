class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = Counter(s)
        maxHeap = [(-v,k) for k,v in counter.items()]
        heapq.heapify(maxHeap)
        res = ''
        # print(maxHeap)
        
        
        temp = []
        while maxHeap: 
            v, k = heapq.heappop(maxHeap)

            res += k 
            v += 1 


            if temp: 
                heapq.heappush(maxHeap, temp.pop())
            if v < 0:
                temp.append((v, k))
            
        if len(res) == len(s): 
            return res 
         
        return ''






        # Passed half of the test cases but not the answer. I was thinking about popping form a maxheap. 
        # counter = Counter(s)
        # maxHeap = [(-v,k) for k,v in counter.items()]
        # heapq.heapify(maxHeap)
        # res = ''
        # # print(maxHeap)
        
       
        # while maxHeap: 
        #     temp = []
        #     while maxHeap: 
        #         v, k = heapq.heappop(maxHeap)

        #         if res and res[len(res)-1] == k:
        #             return ''
        #             break
        #         res += k 
        #         v += 1 

        #         if v < 0:
        #             temp.append((v, k))
        #     for x in temp: 
        #         heapq.heappush(maxHeap, x)
       
        
        # return res

