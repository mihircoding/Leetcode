# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallList = ListNode()
        largeList = ListNode()
        pointS, pointL = smallList, largeList

        while head:
            if head.val < x:
                pointS.next = head
                pointS = pointS.next
            else:
                pointL.next = head
                pointL = pointL.next
            head = head.next
        pointS.next = largeList.next
        pointL.next=  None

        return smallList.next
