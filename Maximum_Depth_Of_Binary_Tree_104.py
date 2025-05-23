# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: list) -> int:
        depth = 0
        stack = []
        lvls = {0: 0}
        while root or stack:
            while root:
                depth += 1
                stack.append(root)
                lvls[root] = depth
                root = root.left
            
            root = stack.pop()
            depth = lvls[root]
            root = root.right

        return max(lvls.values())