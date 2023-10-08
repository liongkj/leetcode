"""
66ms
Beats 85.88%of users with Python3

18.66MB
Beats 10.78%of users with Python3

"""

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val :
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
