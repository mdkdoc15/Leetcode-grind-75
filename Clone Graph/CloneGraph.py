# Created by matthewkight at 7/28/23

import queue

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        visited_nodes = set() # Keep track of what nodes we have already 100% replicated
        created_nodes = {node : Node(val=node.val)} # Old node to new Node
        q = queue.Queue()
        q.put(node)

        while not q.empty():
            cur = q.get()
            if cur in visited_nodes:
                continue
            visited_nodes.add(cur)
            copy_node = created_nodes[cur]
            for adj_node in cur.neighbors:
                if adj_node not in created_nodes:
                    created_nodes[adj_node] = Node(val=adj_node.val)
                copy_node.neighbors.append(created_nodes[adj_node])
                q.put(adj_node)
        return created_nodes[node]



if __name__ == '__main__':
    pass
