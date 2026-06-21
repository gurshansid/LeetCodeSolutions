# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        second = head.next

        while second and second.next:
            first = first.next
            second = second.next.next
    
        secondListHead = first.next
        first.next = None
        prev = None

        while secondListHead:
            temp = secondListHead.next
            secondListHead.next = prev
            prev = secondListHead
            secondListHead = temp
        
        first = head
        second = prev
        
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
          


