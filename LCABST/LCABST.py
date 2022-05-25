# Created by matthewkight at 5/24/22


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val <= root.val <= q.val or q.val <= root.val <= p.val):
            return root
        if (p.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)


if __name__ == '__main__':
    pass
