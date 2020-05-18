# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        oddHead = oddTail = ListNode(None)
        evenHead = evenTail = ListNode(None)
        
        i=1
        while head:
            if i & 1:
                print(oddTail.next)
                oddTail.next = oddTail = head
                print(oddTail.next)
            else:
                evenTail.next = evenTail = head
                
            head = head.next
            
            i += 1
        
        evenTail.next, oddTail.next = None, evenHead.next
        return oddHead.next
