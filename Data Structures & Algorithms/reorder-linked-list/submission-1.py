# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head: ListNode):
            curr = head
            prev = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev

        prev = None
        slow = fast = head
        while slow and fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next

        prev.next = None

        right = reverse(slow)
        left = head
        while right:
            temp = left.next
            left.next = right
            right = right.next
            left = left.next
            left.next = temp
            left = left.next

            
        