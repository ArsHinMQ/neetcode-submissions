# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while slow.next is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                l2 = slow
                break

        l2 = slow.next
        slow.next = None

        prev, curr = None, l2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l2 = prev

        while head is not None and l2 is not None:
            temp = head.next
            head.next = l2
            l2 = l2.next
            head = head.next
            head.next = temp
            head = head.next
