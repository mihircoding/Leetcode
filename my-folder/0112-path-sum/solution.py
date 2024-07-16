# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def recur(root, target):
            if not root:
                return False
            elif not root.right and not root.left and root.val == target:
                return True
            else:
                return recur(root.left,target-root.val) or recur(root.right,target-root.val)
        return recur(root,targetSum)

