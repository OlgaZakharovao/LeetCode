'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: TreeNode) -> list[int]:
    if root is None:
        return []
    l = [root.val]
    l.extend(self.preorderTraversal(root.left))
    l.extend(self.preorderTraversal(root.right))
    return l






root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
