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

        def reverse_linkedlist(l: ListNode):
            curr = l
            prev = None

            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        def extract_n(l: ListNode):
            n = 0
            while l:
                n *= 10
                n += l.val
                l = l.next
            return n

        l1 = reverse_linkedlist(l1)
        l2 = reverse_linkedlist(l2)

        n1 = extract_n(l1)
        n2 = extract_n(l2)

        s = n1 + n2
        if s == 0:
            return ListNode(0)
            
        head = None
        prev = None
        while s:
            val = s % 10
            s = s // 10
            node = ListNode(val)
            if head is None:
                head = node
                prev = head
                continue
            prev.next = node
            prev = node
        return head




        