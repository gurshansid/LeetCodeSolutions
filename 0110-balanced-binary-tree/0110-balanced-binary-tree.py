# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        self.res = True

        def dfs(root, depth):
            if not root:
                return 0
            

            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)

            isBalanced = abs(left - right) <= 1
            
            self.res = self.res & isBalanced

            return 1 + max(left, right)

        dfs(root, 0)
        return self.res
