# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        second = head

        while second and second.next:
            second = second.next.next
            first = first.next
            if first == second:
                return True
        return False
