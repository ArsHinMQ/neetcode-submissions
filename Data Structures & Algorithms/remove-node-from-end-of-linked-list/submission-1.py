# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = head
        total = 0
        while count:
            total += 1
            count = count.next

        if total == 1:
            return None

        counter = 0
        l = head
        prev = None
        while l:
            if total - counter == n:
                l = l.next
                if prev is not None:
                    prev.next = l
                    return head
                return l
            prev = l
            l = l.next
            counter += 1
        return l


                
        