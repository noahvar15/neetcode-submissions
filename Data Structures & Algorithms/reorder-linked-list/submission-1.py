# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ptr1 = head
        stack = self.getStack(head)

        while True:
            ptr2 = stack.pop()

            if ptr1 == ptr2 or ptr1.next == ptr2:
                ptr2.next = None
                break
            next_ptr1 = ptr1.next
            ptr1.next = ptr2
            ptr1 = next_ptr1
            ptr2.next = ptr1

    def getStack(self, head):
        cur = head
        stack = deque()
        while cur is not None:
            stack.append(cur)
            cur = cur.next
        return stack