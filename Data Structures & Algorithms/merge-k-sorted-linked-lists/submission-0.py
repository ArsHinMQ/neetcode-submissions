# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        head = dummy_head
        while True:
            heads = []
            for i, l in enumerate(lists):
                if l is None:
                    continue
                heads.append((l.val, i))
            if not heads:
                return dummy_head.next
            m = min(heads)
            lists[m[-1]] = lists[m[-1]].next
            head.next = ListNode(m[0])
            head = head.next


        