# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        maxSum = float("-inf")
        dummy2 = copy.deepcopy(head)
        dummy = head
        revList = None
        listCount = 0
        while dummy: 
            this = dummy.next 
            dummy.next = revList 
            revList = dummy 
            dummy = this
            listCount += 1 
        listCount = int(listCount / 2)
        
        while listCount > 0:     
            summation = revList.val + dummy2.val      
            maxSum = max(maxSum, summation)
            dummy2 = dummy2.next
            revList = revList.next 
            listCount -= 1 

        return maxSum 
        
    
