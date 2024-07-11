# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        ans = []
        inorder(root,ans)
        return ans
def inorder(node,ans):
    if node is None:
        return
    inorder(node.left,ans)
    ans.append(node.val)
    inorder(node.right,ans)

    

        
