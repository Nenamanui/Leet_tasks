# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root) -> list:
        output_list = []
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            output_list.append(root.val)
            root = root.right
        return output_list