# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        answer = []

        if not root:
            return answer
        
        queue = deque([root])

        while queue:
            listToAdd = []
            levelCount = len(queue)

            for _ in range(levelCount):
                node = queue.popleft()
                listToAdd.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            answer.append(listToAdd)
        return answer

        

        