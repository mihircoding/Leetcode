# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        if not head:
            return head
        dummy = ListNode(0,head)
        pre = dummy
        
        for i in range(left - 1):
            pre = pre.next
        current = pre.next
        for i in range(right-left):
            temp = current.next
            current.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return dummy.next

                        