# Created by matthewkight at 7/28/23
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0))
        out = []
        while len(q) != 0:
            node, level = q.popleft()
            if node is None:
                continue
            q.append((node.left, level+1))
            q.append((node.right, level+1))
            if len(out) > level:
                out[level].append(node.val)
            else:
                out.append([node.val])
        return out
if __name__ == '__main__':
    pass
