'''
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
b = None
l = []

while a.next:
    l.append(a.val)
    a = a.next
l.append(a.val)

for i in range(len(l)):
    b = ListNode(l[i], b)
while b.next:
    print(b.val)
    b = b.next
print(b.val)












