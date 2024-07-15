# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        array = []
        while temp:
            array.append(temp.val)
            temp = temp.next
        ans = []
        l, r = 0, len(array)-1
        while l <= r:
            if l != r:
                ans.append(array[l])
                ans.append(array[r])
                l += 1
                r -= 1
            else:
                ans.append(array[l])
                l += 1
                r -= 1
        temp = head
        i = 0
        while temp and i < len(ans):
            temp.val = ans[i]
            temp = temp.next
            i += 1
        

        


