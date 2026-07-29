# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        dummy_head = ListNode(0)
        prev = dummy_head
        rem = 0
        while l1 or l2 or rem:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            s = v1 + v2 + rem
            rem = 0
            if s > 9:
                rem = s // 10
                s = s % 10
            node = ListNode(s)
            prev.next = node
            prev = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next






        