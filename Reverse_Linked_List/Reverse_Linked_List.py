# Created by matthewkight at 7/28/23
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next:
                self.reverseList(head.next)
                head.next.next = head
                head.next = None
        return head

if __name__ == '__main__':
    pass
