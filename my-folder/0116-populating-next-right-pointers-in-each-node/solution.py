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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        root.next = None
        q = [root]
        ans = root
        print(root.val)
        while q:
            node = q.pop(0)
            if node.left:
                node.left.next = node.right
                if node.next == None:
                    node.right.next = None
                else:
                    node.right.next = node.next.left
                print(node.left.val)
                print(node.right.val)
                q.append(node.left)
                q.append(node.right)
        return ans

