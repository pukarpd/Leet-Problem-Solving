# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # 3 phases 
        dummy = ListNode(0, head )

        Lprev, cur = dummy, head 

        for i in range(left - 1): 
            Lprev, cur = cur, cur.next
        
        prev = None 
        for i in range(right - left + 1): 
            temp = cur.next
            cur.next = prev 
            prev = cur 
            cur = temp

        Lprev.next.next = cur 
        Lprev.next = prev 

        return dummy.next 

        
        
        # # pointers in position
        # leftHead, rightHead = head, head
        # prevL, nextR = ListNode(), rightHead.next
        
        
        # while right > 1: 
        #     if left > 1:
        #         prevL = leftHead
        #         leftHead = leftHead.next
        #         left -= 1
            
        #     rightHead = rightHead.next
        #     right -= 1 
        #     nextR = rightHead.next 
            
        # # print(f"{prevL}\t{leftHead.val}\t{rightHead.val}\t{nextR}")


        # prevL.next, rightHead.next = None,  None
        # dummy = leftHead
        # prev = None 
        # while leftHead:
        #     temp = leftHead.next  
        #     leftHead.next = prev
        #     prev = leftHead
        #     leftHead = temp
        
        # prevL.next, dummy.next = prev, nextR
        
   
        # return prevL.next




