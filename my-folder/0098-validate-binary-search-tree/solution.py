# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [None]
        res = [True]
        self.recur(root,prev,res)
        return res[0]

    def recur(self,node, prev,res):
        if node == None:
            return None
        self.recur(node.left, prev, res)
        if prev[0] and node.val <= prev[0].val:
            res[0] = False
            return None
        prev[0] = node
        self.recur(node.right, prev, res)
        

            
