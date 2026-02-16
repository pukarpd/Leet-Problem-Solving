# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        # Does not work. New approach 
        if not lists:
            return None

        res = ListNode(0)
        dummy = res

        heap = []

        # initialize heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heapq.heappop(heap)
            res.next = node
            res = res.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

        # if not lists: 
        #     return None
        # # O(nlogk solution)

        # # data structures 
        # # return listnode 
        # res = ListNode(0)
        # dummy = res 

        # # maintained with size k 
        # heap = []
        # heapq.heapify(heap)

        # # break conditions 
        # length = len(lists)   # CHANGED: removed null_counter

        # # temp val array of size k which we use to maintain a heap of size k
        # vals = []

        # while True:   # CHANGED: new break logic
        #     active = 0   # CHANGED: count how many lists still alive

        #     for i, l in enumerate(lists):
        #         if l == None: 
        #             continue 
        #         active += 1   # CHANGED
        #         if len(vals) < length:   # CHANGED: use length, not k
        #             vals.append((l.val, i))   # CHANGED: store index
        #             lists[i] = l.next 

        #     if active == 0:   # CHANGED: proper termination
        #         break

        #     while len(heap) < length: 
        #         if not vals: 
        #             break
        #         mini = min(vals)   # tuple compares by value first
        #         heapq.heappush(heap, mini)
        #         vals.remove(mini)

        #     if heap:
        #         val, idx = heapq.heappop(heap)   # CHANGED
        #         temp = ListNode(val)
        #         res.next = temp 
        #         res = res.next 

        # # last bits of heap and val (2 and 1 should remain in each)
        # for val in vals: 
        #     heapq.heappush(heap, val)
        # while heap: 
        #     val, idx = heapq.heappop(heap)   # CHANGED
        #     temp = ListNode(val)
        #     res.next = temp 
        #     res = res.next 

        # return dummy.next




        

        # O(500n) arr appending, O(n) heap building and O(nlogn) pops. Not optimal. logn because the heapo
        # is full of n nodes. but if the heap is just of size k, we can take advantage.  
        # res = ListNode(0)
        # dummy = res 
        # arr = []

        # for l in lists: 
        #     while l: 
        #         arr.append(l.val)
        #         l = l.next
        # heapq.heapify(arr)

        # while arr: 
        #     val = heapq.heappop(arr)
        #     temp = ListNode(val)
        #     res.next = temp 
        #     res = res.next
       
        # return dummy.next
        

         

