# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def recur(root, a):
            if not root:
                return True
            return root.val == a and recur(root.left, a) and recur(root.right,a)
        a = root.val
        return recur(root, a)

