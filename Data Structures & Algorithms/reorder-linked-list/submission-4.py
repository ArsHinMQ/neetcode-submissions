# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        prev = None
        while slow and slow.next and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev is None:
            return
        prev.next = None

        def reverse(head: ListNode):
            cur = head
            prev = None
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        
        right = reverse(slow)
        left = head
        while left and right:
            temp = left.next
            left.next = right
            right = right.next
            left = left.next
            if temp is None:
                left.next = right
                break
            left.next = temp
            left = left.next

            
                
        