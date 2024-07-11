"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return
        curr =head
        og = {}

        while curr is not None:
            og[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr is not None:
            og[curr].next = og.get(curr.next)
            og[curr].random = og.get(curr.random)
            curr = curr.next
        return og[head]
