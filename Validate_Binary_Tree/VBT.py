# Created by matthewkight at 7/29/23

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid_sub_tree(node, max_val, min_val) -> bool:
            if not node:
                return True
            if node.val >= max_val or node.val <= min_val:
                return False
            return valid_sub_tree(node.left, node.val, min_val) and valid_sub_tree(node.right, max_val, node.val)

        if root:
            return valid_sub_tree(root, float('inf'), -float('inf'))

if __name__ == '__main__':
    pass
