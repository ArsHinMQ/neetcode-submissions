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
        while l1 and l2:
            v1 = l1.val
            v2 = l2.val

            s = v1 + v2 + rem
            rem = 0
            if s > 9:
                rem = s // 10
                s = s % 10
            node = ListNode(s)
            prev.next = node
            prev = node
            l1 = l1.next
            l2 = l2.next

        while l1:
            v = l1.val + rem
            rem = 0
            if v > 9:
                rem = v // 10
                v = v % 10
            node = ListNode(v)
            prev.next = node
            prev = node
            l1 = l1.next

        while l2:
            v = l2.val + rem
            rem = 0
            if v > 9:
                rem = v // 10
                v = v % 10
            node = ListNode(v)
            prev.next = node
            prev = node
            l2 = l2.next

        if rem:
            prev.next = ListNode(rem)

        return dummy_head.next






        