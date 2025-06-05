# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 1
        start = head
        if not head:
            return None
        while start.next:
            start = start.next
            length += 1
        start.next = head
        k = length - (k % length)
        for i in range(k):
            start = start.next
        newhead = start.next
        start.next = None
        return newhead


