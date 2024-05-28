'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.


Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: ListNode) -> ListNode:
    counter = 0
    counter2 = 0
    head1 = head
    while head:
        counter += 1
        head = head.next
    if counter % 2 == 0:
        goal = counter // 2
    else:
        goal = int(counter//2)

    while head1 and counter2 < goal:
        counter2 += 1
        head1 = head1.next
    # while head1:
    #     print(head1.val)
    #     head1 = head1.next
    #print(head.val)
    return head1


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(middleNode(head))
