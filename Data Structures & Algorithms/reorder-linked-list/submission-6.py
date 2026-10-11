# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev, slow, fast = None, head, head
        while slow and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev is None:
            return

        prev.next = None

        def reverse(pointer: ListNode):
            cur, prev = pointer, None
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        pl, pr = None, None
        right = reverse(slow)
        left = head
        while right and left:
            pl = left
            temp = left.next
            left.next = right
            left, right = right, temp

        
        
        
        