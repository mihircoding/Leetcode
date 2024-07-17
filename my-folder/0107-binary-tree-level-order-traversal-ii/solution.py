# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        q = [root]
        ans = []
        while q:
            current = []
            length = len(q)
            for i in range(length):
                node = q.pop(0)
                current.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.insert(0,current)
        print(ans)
        return ans
