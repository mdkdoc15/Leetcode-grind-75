# Created by matthewkight at 5/22/22

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.right, root.left = root.left, root.right
        return root

if __name__ == '__main__':
    pass
