# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None
        f = head
        s = head.next
        while f != None and s != None:
            f.val,s.val = s.val,f.val
            
            if s.next == None:
                break
            f = f.next.next
            s = s.next.next
        return head
            
            
