# Created by matthewkight at 5/28/22

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalenced = True
        def height_check(curr) -> int:
            nonlocal isBalenced
            if not curr:
                return -1
            hl = height_check(curr.left)
            hr = height_check(curr.right)
            if not (-1 <= hr - hl <= 1):
                # Is not valid
                isBalenced = False
            return max(hl, hr) + 1

        height_check(root)
        return isBalenced

if __name__ == '__main__':
    pass
