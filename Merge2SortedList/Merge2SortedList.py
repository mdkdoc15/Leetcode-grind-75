# Created by matthewkight at 5/9/22
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        retList = []
        while list1 is not None or list2 is not None:
            if list1 is None:
                # add all the l2 elements
                retList.append(list2.val)
                list2 = list2.next
            elif list2 is None:
                # add all the l2 elements
                retList.append(list1.val)
                list1 = list1.next
            elif list1.val  <= list2.val:
                retList.append(list1.val)
                list1 = list1.next
            else:
                retList.append(list2.val)
                list2 = list2.next

        if len(retList) == 0:
            return list1

        retListHead = ListNode(retList[0])
        walk = retListHead
        for i in range(1, len(retList)):
            walk.next = ListNode(retList[i])
            walk = walk.next
        return retListHead



if __name__ == '__main__':
    pass
