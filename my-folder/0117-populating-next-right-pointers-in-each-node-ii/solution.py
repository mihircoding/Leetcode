"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        root.next = None
        q = [root]
        d = Node(-999)
        while q:
            l = len(q)
            prev = d
            for i in range(l):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    prev.next = node.left
                    prev = prev.next
                if node.right:
                    q.append(node.right)
                    prev.next = node.right
                    prev = prev.next
        return root
