# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        answer = []

        if not root:
            return []
        
        queue = deque([root])

        while queue:
            levelLength = len(queue)
            answer.append(queue[0].val)

            for _ in range(levelLength):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return answer