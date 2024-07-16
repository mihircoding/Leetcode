# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def recur(root,ans):
            if not root:
                return
            ans.append(root.val)
            recur(root.left,ans)
            recur(root.right,ans)
        ans = []
        recur(root,ans)
        return ans
