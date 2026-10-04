# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(n1: int, n2: int):
            div = n1 // n2
            rem = n1 - div*n2
            if rem == 0:
                return n2
            return gcd (n2, rem)

        node = head.next
        prev = head
        while node:
            mid = gcd(max(node.val, prev.val), min(node.val, prev.val))
            prev.next = ListNode(mid, node)
            prev = node
            node = node.next

        return head

        