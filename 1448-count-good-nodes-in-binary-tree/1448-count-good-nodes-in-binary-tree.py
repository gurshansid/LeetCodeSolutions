# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(curr, maxSoFar):
            if not curr:
                return 0
            
            if curr.val >= maxSoFar:
                self.res += 1
            
            dfs(curr.left, max(maxSoFar, curr.val))
            dfs(curr.right, max(maxSoFar, curr.val))
        
        dfs(root, float("-inf"))
        return self.res
            
