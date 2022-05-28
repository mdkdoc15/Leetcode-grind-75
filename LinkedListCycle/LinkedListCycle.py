# Created by matthewkight at 5/28/22

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #
        # O(n) time and space
        #
        # visted = set()
        # while head is not None:
        #     if head in visted:
        #         return True
        #     visted.add(head)
        #     head = head.next
        #
        # return False

        #
        # O(1) space sol attempt
        #

        while head is not None:
            if head.val is None:
                return True
            head.val = None
            head = head.next
        return False
if __name__ == '__main__':
    pass
