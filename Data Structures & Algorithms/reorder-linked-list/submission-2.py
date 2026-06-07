# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge [2, 4, 6] [10, 8] -> 2, 10, 4, 8
        second = prev
        first = head
        while second:
            tmp1 = first.next
            first.next = second
            first = tmp1
            tmp2 = second.next
            second.next = first
            second = tmp2

# use a fast and slow pointer to find the middle of the list.
# reverse the second half of the list.
# alternate between the first half and second half of the list.
# make sure that the last node is pointing to NULL.
        