# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        r = root
        while r:
            if r.val == val:
                return r
            elif r.val < val:
                r = self.searchBST(r.right,val)
            else:
                r = self.searchBST(r.left,val)
            
