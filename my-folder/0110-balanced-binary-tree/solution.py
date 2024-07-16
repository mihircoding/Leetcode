# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(root):
            if not root:
                return 0
            left = recur(root.left) 
            if left < 0:
                return -1
            right = recur(root.right)
            if right < 0:
                return -1
            if abs(left-right) > 1:
                return -1
            return max(left,right) + 1
        return recur(root) >= 0
