"""
45ms
Beats 65.16%of users with Python3

18.59MB
Beats 71.12%of users with Python3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        node = root
        while node is not None:
            max_left =  self.maxDepth(node.left)
            max_right = self.maxDepth(node.right)

            return max(max_left,max_right) + 1
        return 0