# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recur(root,ans):
            if not root:
                return 0 
            ans = (ans * 10) +  root.val
            if not root.left and not root.right:
                return ans
            else:
                return recur(root.left,ans) + recur(root.right,ans) 
        return recur(root,0)
