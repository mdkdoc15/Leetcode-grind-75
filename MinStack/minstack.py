# Created by matthewkight at 7/29/23
import heapq


class MinStack:

    def __init__(self):
        self.data = []
        self.heap = []
    def push(self, val: int) -> None:
        heapq.heappush(self.heap, val)
        self.data.append(val)

    def pop(self) -> None:
        x = self.data.pop()
        self.heap.remove(x)
        heapq.heapify(self.heap)

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.heap[0]

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) # return -3
    minStack.pop()
    print(minStack.top()) # return 0
    print(minStack.getMin()) # return -2
