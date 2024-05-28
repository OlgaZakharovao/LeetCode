'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
and return the new head.


Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head1 = ListNode(0, head)
        cur_head = head1
        while cur_head.next:
            if cur_head.next.val == val:
                cur_head.next = cur_head.next.next
            else:
                cur_head = cur_head.next
        return head1.next
